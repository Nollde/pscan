# PyPScan
PyPScan is a parametric file browser.

Originally developed as "pscan" by the [VISPA Group](https://vispa.physik.rwth-aachen.de).

Now also available in iPython notebooks using pure Python:

![output](https://github.com/user-attachments/assets/d7864b16-2a0f-4632-9fb7-75fd73730c27)

## Usage
```
from pypscan import PyPScan

REGEX_TO_FIND_FILES = (
    r"param0_(?P<param0>.+)"
    r"/param1_(?P<param1>\d+)"
    r"/file\.png"
)
BASE_PATH = "demo/"

pypscan = PyPScan(
    regex=REGEX_TO_FIND_FILES,
    base_path=BASE_PATH,
)

pypscan.run()
```
