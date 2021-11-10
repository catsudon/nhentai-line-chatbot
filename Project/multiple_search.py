from bs4 import BeautifulSoup
import requests
import json
from modules.nhentai import search
from Project.Config import *


def multiple(payload):
    Reply_token = payload['events'][0]['replyToken']
    message = payload['events'][0]['message']['text']

    idx = 1
    try:
        banana = message.split(" ")
        if len(banana) > 1:
            idx = int(banana[len(banana)-1])
            message = ""
            for i in range(len(banana)):
                if i == len(banana)-1:
                    break
                message = message+banana[i]
    except Exception:
        print("no index given")

    idx = idx/2+1 # because line flex message can only contain up to 10 bubble but there are 25 doujins for each page

    data = json.loads(search(message,idx))
   # print(data)
   # print("\n\n\n\n\n")
    reply_payload = []
    title = []
    code = []
    media_id = []
    cnt = 0
    target = 10
    if idx%2==0:
        target = 20

    for item in data['result']:
        if idx%2==0 and cnt < 10:
            cnt=cnt+1
            continue

        print("{}   {} {} {}".format(cnt,item['title']['english'],item['id'],item['media_id']))
        title.append(item['title']['english'])
        code.append(item['id'])
        media_id.append(item['media_id'])

        cnt = cnt + 1
        if cnt == target :
            break

    
    for i in range(len(code)):
        reply_payload.append( con(code[i],title[i],media_id[i])   )


    print(len(reply_payload))
    print("_______________________________")
    if len(reply_payload) == 0:
        print("not found!")
        #nf()
    else:
        LINE_API = 'https://api.line.me/v2/bot/message/reply'

        Authorization = 'Bearer {}'.format(Channel_access_token)
        print(Authorization)
    #    print(reply_payload,indents=4)
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
                        "contents" : (reply_payload)
                    }
                }
            ]
        }


        dt = json.dumps(dt) # from dict to str
    #   print(dt)
        r = requests.post(LINE_API, headers=headers, data=dt) 
        return 200




    

