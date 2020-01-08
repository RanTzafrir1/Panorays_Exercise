from flask import Blueprint, request, jsonify
import requests
from lxml.html import fromstring
import re
from bs4 import BeautifulSoup

class metadata:

    #Class attributes
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }
    timeout = 5
    response = {
        "status": 200
    }

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url, timeout=5, headers=self.HEADERS)
        

    def getTitle(self):
        return fromstring(self.response.content).findtext('.//title')

    def getLandingPage(self):
        return self.url

    def getGoogleAnalyticsId(self):
        soup = BeautifulSoup(self.response.text, 'html.parser')
        all_scripts = soup.find_all('script')
        for script in all_scripts:
            if script.text.find("UA-") > 0:
                word = script.text
                index = word.find("UA-")
                text = word[index:index+20]
                print(text.split("',")[0])
        return text.split("',")[0]