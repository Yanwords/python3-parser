import os
import unittest
from test import support

# Skip this test if _tkinter wasn't built.
support.import_module('_tkinter')

# Make sure tkinter._fix runs to set up the environment
support.import_fresh_module('tkinter')

# Skip test if tk cannot be initialized.
support.requires('gui')

from _tkinter import TclError
from tkinter import ttk
from tkinter.test import runtktests
from tkinter.test.support import get_tk_root

try:
    ttk.Button()
except TclError as msg:
    # assuming ttk is not available
    raise unittest.SkipTest("ttk not available: %s" % msg)

def test_main():
    try:
        support.run_unittest(
                *runtktests.get_tests(text=False, packages=['test_ttk']))
    finally:
        get_tk_root().destroy()

if __name__ == '__main__':
    test_main()
