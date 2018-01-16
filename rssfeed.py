from flask import Flask, render_template, request, redirect
import feedparser
import time

app = Flask(__name__)

list = ["https://xkcd.com/rss.xml"]
feedtoprint = []

@app.route('/')
def rssFeed():
    author = "Logan Fladung"
    return render_template('index.html', author=author, list=list, feedtoprint=feedtoprint)

@app.route('/addToList', methods = ['POST'])
def addToList():
    url = request.form['URL']
    list.append(url)
    return redirect('/')

@app.route('/printRSS', methods = ['POST'])
def printRSS():
    url = request.form['URL']
    feed = feedparser.parse(url)
    count = 1
    for post in feed.entries:
        if count % 5 == 1:
            feedtoprint.append("\n Loaded at " + time.strftime('%H:%M:%S'))
        feedtoprint.append(post.title + "\n")
        feedtoprint.append(post.link + "\n")
        feedtoprint.append(post.description + "\n") 
        feedtoprint.append(post.published + "\n")
        feedtoprint.append("----------------------\n")
        count += 1
    return redirect('/')


if __name__ == '__main__':
    app.run()
