import sys
import unittest
from typing import Optional


class Checker:
    def version(self):
        major: Optional[int] = sys.version_info[0]
        minor: Optional[int] = sys.version_info[1]
        print("Version : " + str(major) + "." + str(minor) + " : ", id(self))


class VersionTest(unittest.TestCase):
    @classmethod
    def setupClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.checker = Checker()
        print("setUp", id(self))

    def tearDown(self):
        # self.checker.version()
        print("tearDown", id(self))

    def test_check_major(self):
        py_major: Optional[int] = sys.version_info[0]
        major_calc = int(py_major)
        set_major = int(4)
        print("test_check", id(self))
        self.assertLess(major_calc, set_major)

    def test_check_minor(self):
        py_minor: Optional[int] = sys.version_info[1]
        minor_calc = int(py_minor)
        set_minor = int(0)
        print("test_check", id(self))
        self.assertGreater(minor_calc, set_minor)


if __name__ == '__main__':
    unittest.main()
