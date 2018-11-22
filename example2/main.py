from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import requests

class Downloader(QDialog):

    def __init__(self):
        super(Downloader,self).__init__()
        layout =  QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText('URL')

        self.save_location = QLineEdit()
        self.save_location.setPlaceholderText('File save location')

        self.progress = QProgressBar()
        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        downloadbtn = QPushButton('Download')
        browse = QPushButton('Browse')

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(downloadbtn)

        self.setLayout(layout)
        self.setWindowTitle('PyDownloader')
        self.setFocus()

        downloadbtn.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption='Save file as',directory='C:\\',filter='All Files (*.*)')
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        session = requests.Session()
        try:
            urlWithProtocol = str(self.url.text())
            if(not(urlWithProtocol.startswith('http'))):
                urlWithProtocol = 'http://' + urlWithProtocol
            response = session.get(urlWithProtocol, stream=True)

        except Exception as e:
            print(e)
            QMessageBox.warning(self,'Warning','Download failed')
            return
        total_length = response.headers.get('content-length')

        with open(self.save_location.text(), "wb") as f:
            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                received_length = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    received_length += len(data)
                    f.write(data)
                    self.report(received_length,total_length)

        QMessageBox.information(self,'Information','The download is complete!')
        self.progress.setValue(0)

    def report(self,received_length,total_length):
        percent = (received_length * 100)/total_length
        self.progress.setValue(int(percent))

app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
sys.exit(app.exec_())
