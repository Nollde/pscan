# PScan
PScan is a parametric file browser.

Originally developed by the [VISPA Group](https://vispa.physik.rwth-aachen.de).

Now also available in iPython notebooks using pure Python:

![output](https://github.com/user-attachments/assets/829855aa-002a-4cd2-a253-a02f3a15d8eb)


## Usage
```
from pscan import PScan

REGEX_TO_FIND_FILES = (
    r"param0_(?P<param0>.+)"
    r"/param1_(?P<param1>\d+)"
    r"/file\.png"
)
BASE_PATH = "demo/"

pscan = PScan(
    regex=REGEX_TO_FIND_FILES,
    base_path=BASE_PATH,
)

pscan.run()
```