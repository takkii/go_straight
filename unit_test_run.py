import sys
import unittest
from typing import Optional


class VersionTest(unittest.TestCase):
    def test_check(self):
        py_major: Optional[int] = sys.version_info[0]
        py_minor: Optional[int] = sys.version_info[1]

        # print(py_major)
        # print(py_minor)

        major_calc = int(py_major)
        minor_calc = int(py_minor)

        set_major = int(4)
        set_minor = int(0)

        self.assertLess(major_calc, set_major)
        self.assertGreater(minor_calc, set_minor)


if __name__ == '__main__':
    unittest.main()
