from Project.Config import *
import json
from modules.nhentai import getBookById
import requests
from bs4 import BeautifulSoup

def preview(payload):
    Reply_token = payload['events'][1]['replyToken']
    message = payload['events'][1]['message']['text']
    message = message[3:]
    print(f"preview {message}")
    book = json.loads(getBookById(message))

    mx_page = len(book['images']['pages'])
    print(mx_page)

    payload = []

    for i in range(1,mx_page,int(mx_page/10)+1):
        r = requests.get(f"https://nhentai.net/g/{message}/{i}/")
        soup = BeautifulSoup(r.text,"html.parser")
        a = soup.find_all('img')
        payload.append(con3(a[1]['src']))
        print(a[1]['src'])
        if(len(payload)==5):
            break


    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Channel_access_token)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': Authorization
    }

    dt = {
        "replyToken":Reply_token,
        "messages":
        [
            {
                "type": "flex",
                "altText": "Not safe for work",
                "contents": 
                {
                    "type" : "carousel",
                    "contents" : (payload)
                }
            }
        ]
    }


    dt = json.dumps(dt) # from dict to str
    r = requests.post(LINE_API, headers=headers, data=dt) 
    return 200
