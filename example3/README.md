# Example 3
Simple dialog with two event handlers (textChanged and clicked) as in example 1, but designed with QTDesigner application
Followed the below steps:
* With the installed `pyqt5-tools`, QTDesigner application `designer.exe` will be available under `<Python installation>Scripts` or `<Python installation>\Lib\site-packages`. Adding this path to your PATH environment variable will make things easier.
* Generated code from `helloworld.ui` as below
```
  pyuic5 helloworld.ui > helloword_ui.py
```
* `Ui_Dialog` class in generated code utilized in main.py

![alt text](https://raw.githubusercontent.com/aliakyurek/python-gui/master/example3/image.png)
