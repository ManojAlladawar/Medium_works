import requests

class Browsers:

    def __int__(self):
        self.session = requests.session()

    def get(self, url, headers = None):
        headers = headers or {}
        return self.session.get(url, headers = headers)
    
    def post(self, url, data=None, header=None):
        headers = headers or {}
        return self.session.post(url, data=data, headers = headers)

        