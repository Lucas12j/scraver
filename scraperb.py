from bs4 import BeautifulSoup
import re
import requests

class ScraperB():

    def __init__(self, url, cssSelector, regex = '.+'):

        self.regex = regex

        if "tbody" in cssSelector:
            cssSelector = cssSelector.replace("tbody > ","")

        agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        r = requests.get(url, headers = agent)
        self.value  = str(BeautifulSoup(r.text, 'lxml').select(cssSelector)).replace("\n","")

    def getValue(self):
        value = re.findall(self.regex, self.value)
        if len(value) == 0:
            return "SyntaxError Regex", 406
        elif len(value) == 1:
            return value[0],200
        elif len(value) > 1:
            return value, 200

