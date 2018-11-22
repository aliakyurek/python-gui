from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class HelloWorld(QDialog):
    def __init__(self):
        super(HelloWorld,self).__init__()

        layout =  QGridLayout()

        self.label = QLabel("Hello World!")
        line_edit = QLineEdit()
        button = QPushButton("Close")

        # layout.addWidget(self.label)
        layout.addWidget(self.label,0,0) # grid layout
        # layout.addWidget(line_edit)
        layout.addWidget(line_edit,1,0) # grid layout
        # layout.addWidget(button)
        layout.addWidget(button,2,0) #grid layout
        self.setLayout(layout)

        button.clicked.connect(self.close)
        # line_edit.textChanged.connect(self.label.setText)
        line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.label.setText(text)


app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
sys.exit(app.exec_())
