import requests
import os
from requests_ntlm import HttpNtlmAuth


class MainModel:
    def __init__(self,url,local_path):
        if(not(url.startswith('http'))):
            url = 'http://' + url
        self.url = url
        self.local_path = local_path
        pass

    def statusChanged(self,func):
        self.cbStatusChanged = func

    def handleAuthentication(self,session):
        if(os.environ.get('PROXY_USER') and os.environ.get('PROXY_PASS')):
            # get rid of double \\ if exists in user name (for ex. DOMAIN\account) using unicode-escape
            print('Enabling NTLM authentication using credentials {}:****'.format(os.environ.get('PROXY_USER').encode('ascii').decode('unicode-escape')))
            session.auth = HttpNtlmAuth(os.environ.get('PROXY_USER').encode('ascii').decode('unicode-escape'),
            os.environ.get('PROXY_PASS').encode('ascii').decode('unicode-escape'),
            session)        

    def startDownload(self):
        session = requests.Session()
        self.handleAuthentication(session)

        try:
            response = session.get(self.url, stream=True)

        except Exception as e:
            print(e)
            return

        total_length = response.headers.get('content-length')

        with open(self.local_path, "wb") as f:
            if total_length is None:  # no content length header
                f.write(response.content)
                self.report(100,100)
            else:
                received_length = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    received_length += len(data)
                    f.write(data)
                    self.report(received_length,total_length)

    def report(self,received_length,total_length):
        percent = (received_length * 100)/total_length
        self.cbStatusChanged(int(percent))

