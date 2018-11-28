import sys
import urllib
import requests
from requests_ntlm import HttpNtlmAuth
from lib.requests_ntlmsspi import HttpNtlmSspiAuth
# from lib.requests_ntlmsspi import HttpNtlmSspiAuth

class Download:
    def __init__(self):
        self.__username = ''
        self.__password = ''
        self.__url = 'http://ipv4.download.thinkbroadband.com/5MB.zip'
        self.__saveLocation = 'c:\\download'
        self.__autoConnect = True
        self.__proxyAddress = {
            'http': None,
            'https': None
        }
        self.callbacks = {
            'transferProgressChanged': None,
            'autoConnectChanged': None
        }
        proxies = urllib.request.getproxies()
        if('http' in proxies):
            self.__proxyAddress['http'] = proxies['http']

        if('https' in proxies):
            self.__proxyAddress['https'] = proxies['https']

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value
        sys.stdout.write('\rusername changing:[%s]' % (self.__username))

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
        sys.stdout.write('\rPassword changing:[%s]' % (self.__password))

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        if(not(value.startswith('http'))):
            value = 'http://' + value
        self.__url = value
        sys.stdout.write('\rUrl changing:[%s]' % (self.__url))

    @property
    def saveLocation(self):
        return self.__saveLocation

    @saveLocation.setter
    def saveLocation(self, value):
        self.__saveLocation = value
        sys.stdout.write('\rSave location changing:[%s]' % (self.__saveLocation))

    @property
    def autoConnect(self):
        return self.__autoConnect

    @autoConnect.setter
    def autoConnect(self, value):
        self.__autoConnect = value
        if(self.callbacks['autoConnectChanged']):
            self.callbacks['autoConnectChanged'](self.__autoConnect)
        sys.stdout.write('\rAuto connect changing:[%s]' % (self.__autoConnect))

    @property
    def proxyAddress(self):
        return self.__proxyAddress

    @proxyAddress.setter
    def proxyAddress(self, value):
        self.__proxyAddress = value
        sys.stdout.write('\rProxy addresses changing:[%s]' % (self.__proxyAddress))

    def bind(self, event, func):
        self.callbacks[event] = func

    def handleAuthentication(self,session):
        if(self.__autoConnect):
            session.auth = HttpNtlmSspiAuth()
        else:
            print(self.__username,self.__password)
            session.auth = HttpNtlmAuth(self.__username,self.__password)

    def startDownload(self):
        session = requests.Session()
        self.handleAuthentication(session)

        try:
            response = session.get(self.url, stream=True)

        except Exception as e:
            print(e)
            return

        total_length = response.headers.get('content-length')

        with open(self.__saveLocation, "wb") as f:
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
        self.callbacks['downloadProgressChanged'](int(percent))

