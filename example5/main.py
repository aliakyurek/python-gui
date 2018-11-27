import sys
from PyQt5.QtWidgets import QApplication
import controllers.main

'''
Different import schmese
>>> import pkg.mod1, pkg.mod2
>>> pkg.mod1.foo()

>>> from pkg.mod1 import foo
>>> foo()

>>> from pkg import mod1
>>> mod1.foo()
'''

class PyDownloader(QApplication):
    def __init__(self, sys_argv):
        super(PyDownloader, self).__init__(sys_argv)
        # if controllers.main.Download instance not assigned to a class variable
        # it's automatically disposed and hence dialog is closed
        self.main_ctrl = controllers.main.Download()

if __name__ == '__main__':
    app = PyDownloader(sys.argv)
    sys.exit(app.exec_())
