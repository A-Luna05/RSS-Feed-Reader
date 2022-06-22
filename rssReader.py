# Author: Albert Luna
# Copying of this code is prohibited.
# Github: https://github.com/A-Luna05

import feedparser;
from articleObject import articleObject

class NewsCollection:
    def __init__(self):
        self.rssDict = {}
        sourceFile = open('newsSources.txt', 'r')
        while True:
            line = sourceFile.readline()
            if not line:
                break
            feedItems = line.split(',')
            self.rssDict[feedItems[0]] = feedparser.parse(feedItems[1])
        sourceFile.close()
        self.run = True
        self.postList = []
        self.processedPostList = []
        for keys in self.rssDict.keys():
            self.getPosts(keys)
        self.postList.sort(key = lambda x: x.weight)

    def addFeed(self,entryName,entryFeed):
        self.rssDict.update({entryName:feedparser.parse(entryFeed)})
        self.getPosts(entryName)
        self.postList.sort(key = lambda x: x.weight)
        sourceFile = open('newsSources.txt', 'a')
        sourceFile.write(entryName + ',' +entryFeed+ '\n')
        sourceFile.close()

    def getPosts(self,name):
        feed = self.rssDict.get(name)
        posts = feed.entries
        weight = 0
        for article in posts:

            temp = articleObject(article.link)
              
            try:
                temp.weight = weight
                weight += 1
                temp.title = article.title
                temp.tags = [tag.term for tag in article.tags]
                temp.summary = article.summary
            except:
                pass

            self.postList.append(temp)
