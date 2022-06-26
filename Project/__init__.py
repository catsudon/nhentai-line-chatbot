from flask import Flask , request , abort
import requests
import json
from Project.Config import *
from Project.preview import *
from modules.nhentai import getBookById
from Project.multiple_search import multiple
import base64
from io import BytesIO
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        print(payload)

        try:
            temp = payload['events'][1]
            Reply_token = payload['events'][1]['replyToken']
            message = payload['events'][1]['message']['text']
            preview(Reply_token,message)
        except Exception:

            message = payload['events'][0]['message']['text']
            
            if(message == "วิธีใช้งาน"):
                return request.json, 200
            
            if(message.isdigit()):
                 one_by_one(payload)
            # elif(message[0:2] == '@p'):
            #     preview(payload['events'][0]['replyToken'] , message)
            #     print("reply timeout")
            else:
                print("call multiple")
                multiple(payload)
        
          
          
        return request.json, 200

    elif request.method == 'GET' :
        r = requests.get("https://nhentai.net")
        return r.text , 200

    else:
        abort(400)

def one_by_one(payload):
      
    Reply_token = payload['events'][0]['replyToken']
    message = payload['events'][0]['message']['text']

    book = getBookById(message)
    try:
        title = book['data']['nhentai']['by']['mediaId']
    except KeyError:
        nf(Reply_token)
        return 404
    img = book
    title = book['data']['nhentai']['by']['title']['display']
    code = str(book['data']['nhentai']['by']['id'])
    w = str(book['data']['nhentai']['by']['images']['cover']['w'])
    h = str(book['data']['nhentai']['by']['images']['cover']['h'])

    print(img,title,code,w,h)

    ReplyMessage(Reply_token ,img, title, code, w, h)
    return 200



def ReplyMessage(Reply_token,img, title, code, w, h):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    print(code)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[{
            "type": "flex",
            "altText": "NSFW",
            "contents": con2(img, title, code, w , h)
    }]}

    data = json.dumps(data) ## dump dict >> string
    r = requests.post(LINE_API, headers=headers, data=data)

    # notify creator
    log(code,title)

    return 200

@app.route('/')
def hello():
    return "<marquee>IT'S WORKING</marquee>",200

if __name__ == "__main__":
    app.run(debug=True)