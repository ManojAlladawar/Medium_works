import requests

class Browsers:
    def __init__(self):
        self.session = requests.session()
    
    def get(self, url):
        return self.session.get(url)
    
    def post(self,url,data=None):
        return self.session.post(url, data=data)

        