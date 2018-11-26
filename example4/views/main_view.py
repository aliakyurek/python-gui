import sys

class MainView:
    def __init__(self):
        pass

    def show(self):
        print('Downloader started')

    def setProgress(self,percent):
        sys.stdout.write('\r[{}{}]:{}%'.format('=' * percent, ' ' * (100 - percent),percent))
