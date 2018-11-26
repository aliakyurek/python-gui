import sys
from controllers.main_controller import MainController
from dotenv import load_dotenv, find_dotenv

class Downloader():
    def __init__(self, sys_argv):
        self.main_ctrl = MainController(sys_argv)

if __name__ == '__main__':
    dotenv_path = find_dotenv()
    if(dotenv_path):
        load_dotenv(dotenv_path)
    app = Downloader(sys.argv)
