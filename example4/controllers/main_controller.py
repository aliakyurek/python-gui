from models.main_model import MainModel
from views.main_view import MainView

class MainController:
    def __init__(self, sys_argv):
        self.model = MainModel(sys_argv[1],sys_argv[2])
        self.model.statusChanged(self.transferStatusChanged)

        self.view = MainView()
        self.view.show()
        self.model.startDownload()

    def transferStatusChanged(self,percent):
        self.view.setProgress(percent)