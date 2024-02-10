import gc
import sys

from typing import Optional

try:
    # It doesn't support python4 yet.
    py_major: Optional[int] = sys.version_info[0]
    py_minor: Optional[int] = sys.version_info[1]

    # 3.5 or higher and 3.12 or less python version is required.
    if (py_major == 3 and py_minor < 12) and (py_major == 3 and py_minor > 4):
        print('--------------------------------------------------------------')

        # Run, unit/xunit.py
        with open('./unit/xunit.py') as xut:
            xcmd = xut.read()
            exec(xcmd)

        print('--------------------------------------------------------------')

        # Run, unit/unit.py
        with open('./unit/unit.py') as ut:
            cmd = ut.read()
            exec(cmd)

    # Python Version 3.12 or less.
    else:
        raise ValueError("Python Version Check, 3.12 or less.")

except Exception as ext:
    print(ext)
    raise RuntimeError from None

finally:
    # GC collection.
    gc.collect()
