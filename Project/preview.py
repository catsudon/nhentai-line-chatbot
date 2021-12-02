from Project.Config import *
import json
from modules.nhentai import getBookById
import requests
from bs4 import BeautifulSoup

def preview(Reply_token , message):
    message = message[3:]
    print(f"preview {message}")
    book = json.loads(getBookById(message))

    mx_page = len(book['images']['pages'])
  #  print(mx_page)

    sauce = requests.get(f"https://nhentai.net/g/{message}/")
    soup = BeautifulSoup(sauce.text,"html.parser")
    a = soup.find_all('img')[2]['src']

    sauce = ""
    ar = a.split('/')
    br = False
    for components in ar:
        sauce = sauce+components+'/'
        if(br):
            break
        if(components == "galleries"):
            br=True

    payload = []

    for i in range(1,mx_page,int(mx_page/10)+1):
        src = sauce+str(i)+"t.jpg"
        payload.append(con3(src))
        print(src)
        if(len(payload)==6):
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
    requests.post(notify_url, headers=notify_headers, data = {'message': "prev : " + message})
    return 200
