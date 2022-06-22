from tkinter import *
import webbrowser
from PIL import Image, ImageTk
import requests
import io

from rssReader import NewsCollection
global photoList
photoList = []

class newsAggregate(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.title('Reader')
        self.newsCollection = NewsCollection()
        self.articleCursor = 0
        self.articleTotal = len(self.newsCollection.postList) 
        self.articleList = []  
        self.currentPage = 1 
        self.pageCount = 1 + len(self.newsCollection.postList)/8     
        self.make_widgets()

    def make_widgets(self):
        self.b1 = Button(self,text='Add a \n Feed',bg= '#90EE90',command=lambda:self.popup())
        self.b1.grid(column=0,row=0,sticky='n')
        self.b2 = Button(self,text='< Prev',command=lambda:self.change_feed(1))
        self.b2.grid(column=0,row=1,sticky='s')
        self.b3 = Button(self,text='Next >',command=lambda:self.change_feed(2))
        self.b3.grid(column=3,row=1,sticky='s')
        self.articlesFrame1 = Frame(self)
        self.articlesFrame2 = Frame(self)
        self.articleList.append(Frame(self.articlesFrame1))
        self.articleList.append(Frame(self.articlesFrame1))
        self.articleList.append(Frame(self.articlesFrame1))
        self.articleList.append(Frame(self.articlesFrame1))
        self.articleList.append(Frame(self.articlesFrame2))
        self.articleList.append(Frame(self.articlesFrame2))
        self.articleList.append(Frame(self.articlesFrame2))
        self.articleList.append(Frame(self.articlesFrame2))
        self.change_feed(0)

    def change_feed(self,direction):
        photoList.clear()
        if direction == 0:
            self.articleCursor = 0
            self.articlesFrame1.grid(column=1,row=0)
            self.articlesFrame2.grid(column=2,row=0)
        elif direction == 2:
            self.currentPage = self.currentPage + 1
        elif direction == 1 and self.articleCursor >= 8:
            self.currentPage = self.currentPage - 1
            self.articleCursor = self.articleCursor - 16
        else:
            return

        for x in range(8):
            try:
                articleNum = self.articleCursor
                if self.newsCollection.postList[articleNum].processed == False:
                    self.newsCollection.postList[articleNum].getInfo()
                currentArticle = self.articleList[x]
                for widgets in currentArticle.winfo_children():
                    widgets.destroy()
                infoFrame = Frame(currentArticle)
                Label(infoFrame,text=self.newsCollection.postList[articleNum].title,font=('Sitka bold',14),wraplengt=350).pack()
                Label(infoFrame,text=self.newsCollection.postList[articleNum].summary,font=('sitka',11),wraplengt=350).pack()
                link = Label(infoFrame,text=self.newsCollection.postList[articleNum].link,wraplengt=350,font=('sitka',10),fg='#0000EE')
                link.pack()
                link.bind("<Button-1>", lambda e, url=self.newsCollection.postList[articleNum].link: webbrowser.open_new(url))
                infoFrame.grid(column=1,row=0)
                r = requests.get(self.newsCollection.postList[articleNum].top_image)
                pilImage = Image.open(io.BytesIO(r.content))
                pilImage.thumbnail((180,180))
                image = ImageTk.PhotoImage(pilImage)
                photoList.append(image)
                Label(currentArticle,image=photoList[x],wraplength=100,height = 130,width=130).grid(column=0,row=0)
                currentArticle.pack()
                self.articleCursor = self.articleCursor + 1
                postCount = len(self.newsCollection.postList)
            except:
                break
        Label(self,text = "Article Count: %d" %(postCount)).grid(column=2,row=1,sticky='n')
        Label(self,text = "Page %d of %d" %(self.currentPage,self.pageCount)).grid(column=1,row=1,sticky='n')      
    
    def popup(self):
        self.top= Toplevel(self)
        self.top.geometry("400x80")
        self.top.title("Add a New Feed")
        Label(self.top,text="Name of Feed").grid(column=0,row=0)
        ent1 = Entry(self.top,width = 10)
        ent1.grid(column = 1, row = 0)
        Label(self.top,text="RSS Feed Url").grid(column=0,row=1)
        ent2 = Entry(self.top,width = 50)
        ent2.grid(column = 1, row = 1)
        addFeed = Button(self.top,text='Add Feed',bg= '#90EE90',command=lambda:self.addNewFeed(ent1.get(),ent2.get()))
        addFeed.grid(column=1,row=2)
    
    def addNewFeed(self,name,url):
        self.newsCollection.addFeed(name,url)
        self.top.destroy()
        self.pageCount = 1 + len(self.newsCollection.postList)/8     
        self.change_feed(0)

def callback(url):
    webbrowser.open_new_tab(url)
