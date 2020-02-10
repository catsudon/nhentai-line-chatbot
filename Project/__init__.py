from flask import Flask , request , abort
import requests
import json
from Project.Config import *
from flask_cors import CORS
from flask_compress import Compress
from modules.nhentai import search,getBookById

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

        for i in range (len(book["tags"])):
            print(book["tags"][i]["name"])
            # Reply_messasge = book["tags"][i]["name"]
            # ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        title = book["title"]['english']
        Reply_messasge = json.dumps(title)
        print(Reply_messasge)
        ReplyMessage(Reply_token,Reply_messasge,Channel_access_token,message)
        
        
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 'hello world',200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token , num):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format('7VhCJLogwUjrZjNtOXuXK7aqVWK7/vHKW5A1TdNnD4eFzoBOL8bM8ukFqD8QEsRPnkfO4TmwIZ2AREUEOTme4ijk6xbFnBmhNK0maDYizUVw96x0ZHAe95BTG9SuCsMB4mbY8/z9nxXcgos9fTJ8jgdB04t89/1O/w1cDnyilFU=')
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
"type": "template",
  "altText": TextMessage,
  "template": {
    "type": "carousel",
    "actions": [],
    "columns": [
      {
        "thumbnailImageUrl": "https://i.nhentai.net/galleries/"+ num +"/1.jpg",
        "title": TextMessage,
        "text": "nhentai.net/"+num,
        "actions": [
          {
            "type": "uri",
            "label": "READ",
            "uri": "https://nhentai.net/" + num
          }
        ]
      }
    ]
  }
}]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200

if __name__ == "__main__":
    app.run(debug=True)