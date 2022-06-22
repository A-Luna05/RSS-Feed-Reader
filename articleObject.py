# Author: Albert Luna
# Copying of this code is prohibited.
# Github: https://github.com/A-Luna05
from newspaper import Article
class articleObject(Article):

    def __init__(self,url):
        Article.__init__(self,url)
        self.weight = 0
        self.summary = ""
        self.link = url
        self.processed = False


    def getInfo(self):
        self.download()
        self.parse()
        self.processed = True

    def __str__(self):
        return self.title + "\n" + self.summary + "\n" + self.link + "\n" +self.top_image