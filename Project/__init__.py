from flask import Flask , request , abort
import requests
import json
from Project.Config import *
from Project.preview import *
from modules.nhentai import getBookById
from Project.multiple_search import multiple
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        try:
            temp = payload['events'][1]
            Reply_token = payload['events'][1]['replyToken']
            message = payload['events'][1]['message']['text']
            preview(Reply_token,message)
        except Exception:
            message = payload['events'][0]['message']['text']
            if(message.isdigit()):
                one_by_one(payload)
            elif(message[0:2] == '@p'):
                preview(payload['events'][0]['replyToken'] , message)
                print("reply timeout")
            else:
                multiple(payload)
        
          
          
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

def one_by_one(payload):
      
    Reply_token = payload['events'][0]['replyToken']
    message = payload['events'][0]['message']['text']

    book = json.loads(getBookById(message))
    title = book['title']['english']
    img = book['media_id']
    w = book['images']['cover']['w']
    h = book['images']['cover']['h']

    Reply_message = json.dumps(title)

    ReplyMessage(Reply_token,Reply_message,Channel_access_token,message,img,w,h)
      



def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token , num, img , w , h):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    print(num)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type": "flex",
            "altText": "Not safe for work",
            "contents": con2(num,TextMessage,img,w,h)
    }]}

    data = json.dumps(data) ## dump dict >> string
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200

@app.route('/')
def hello():
    return 'hello world',200

if __name__ == "__main__":
    app.run(debug=True)