import re
import requests

class Browseer:
    def get(self, url):
        return requests.get(url)
    
    def post(self, url, data=None):
        return requests.post(url,data=data)