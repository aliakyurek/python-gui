import sys
from PyQt5.QtWidgets import QDialog, QApplication
from helloworld_ui import Ui_Dialog

class HelloWorld(QDialog):
    def __init__(self):
        super(HelloWorld,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.close)
        # line_edit.textChanged.connect(self.label.setText)
        self.ui.lineEdit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.ui.label.setText(text)

app = QApplication(sys.argv)
w = HelloWorld()
w.show()
sys.exit(app.exec_())