from flask import Flask , request , abort
import requests
import json
from Project.Config import *
from flask_cors import CORS
from flask_compress import Compress
from modules.nhentai import search,getBookById
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)
Compress(app)


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json


        Reply_token = payload['events'][0]['replyToken']
        message = payload['events'][0]['message']['text']
        print(message)
        book = json.loads(getBookById(message))
        print(book)



        import requests
        url = "https://nhentai.net/g/"+message
        data = requests.get(url)
###############

        soup = BeautifulSoup(data.text,'html.parser')
        x = soup.find_all("img",{"class":""})
        q=0
        for image in x:
    #print image source
            print(image['src'])
            if q == 1 :
                img = image['src']
                break
            q=q+1


        for i in range (len(book["tags"])):
            print(book["tags"][i]["name"])

        title = book["title"]['english']
        Reply_messasge = json.dumps(title)
        print(Reply_messasge)
        ReplyMessage(Reply_token,Reply_messasge,Channel_access_token,message,img)
        
        
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token , num, img):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format('7VhCJLogwUjrZjNtOXuXK7aqVWK7/vHKW5A1TdNnD4eFzoBOL8bM8ukFqD8QEsRPnkfO4TmwIZ2AREUEOTme4ijk6xbFnBmhNK0maDYizUVw96x0ZHAe95BTG9SuCsMB4mbY8/z9nxXcgos9fTJ8jgdB04t89/1O/w1cDnyilFU=')
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[
            {
  "type": "flex",
  "altText": "Not safe for work",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
      "type": "image",
      "url": img,
      "size": "full",
      "aspectRatio": "350:506",
      "aspectMode": "fit",
      "backgroundColor": "#6A0707"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": TextMessage[1:41],
          "size": "xl",
          "align": "start",
          "gravity": "top",
          "color": "#3E2929"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "READ",
            "uri": "https://nhentai.net/g/"+num
          },
          "flex": 6,
          "color": "#4AA394",
          "margin": "xs",
          "height": "md",
          "style": "primary",
          "gravity": "top"
        }
      ]
    }
  }
}
     ]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200

if __name__ == "__main__":
    app.run(debug=True)