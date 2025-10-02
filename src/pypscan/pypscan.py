import re
import os
from collections import defaultdict, OrderedDict

from IPython.display import display
from wand.image import Image as WImage
import ipywidgets as widgets
from ipywidgets import interact

from .utils import SKDict


class PyPScan:
    def __init__(self, regex, base_path="./"):
        self.regex = regex
        self.base_path = base_path
        self.skdict = self._scan(base_path)
        self._create_controls()

    def _scan(self, base_path):
        skdict = SKDict()
        for root, dirs, files in os.walk(base_path):
            for file in files:
                path = os.path.join(root, file)
                search = re.search(self.regex, path)
                if search is None:
                    continue
                skdict[search.groupdict()] = path
        return skdict

    def _get_options(self, skdict, sort=True):
        opt = defaultdict(set)
        for _opt in skdict.keys():
            for key, value in dict(_opt).items():
                opt[key].add(value)
        if sort:
            for key in opt:
                opt[key] = sorted(opt[key])
            opt = OrderedDict(sorted(opt.items()))
        return opt

    def _create_controls(self):
        self.controls = {}
        sorted_options = self._get_options(self.skdict)
        for key, values in sorted_options.items():
            self.controls[key] = widgets.ToggleButtons(
                description=key,
                options=values,
            )

    def display_content(self, path):
        """
        Display contant at path.
        Overwrite to display custom formats.
        """
        if path.lower().endswith(('.txt')):
            with open(path, "r") as f:
                content = f.read()
            display(content)
        elif path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.pdf')):    
            image = WImage(filename=path)
            display(image)
        else:
            print(f"Unsupported file type: {path}")

    def _display(self, **kwargs):
        path = self.skdict[kwargs]
        self.display_content(path)

    def _update_options(self, change):
        for key, control in self.controls.items():
            value = control.value
            options = self._get_options(
                self.skdict[{k: v.value for k, v in self.controls.items() if k != key}]
            )
            control.options = sorted(options[key])
            control.value = value

    def run(self):
        interact(self._display, **self.controls)
        self._update_options(None)
        for key, control in self.controls.items():
            control.observe(self._update_options)
