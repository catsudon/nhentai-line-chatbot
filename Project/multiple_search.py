# from bs4 import BeautifulSoup
# import requests
# import json
# from modules.nhentai import search
# from Project.Config import *


# def multiple(payload):
#     Reply_token = payload['events'][0]['replyToken']
#     message = payload['events'][0]['message']['text']
#     print(message)
#     idx = 1
#     try:
#         banana = message.split(" ")
#         if len(banana) > 1:
#             idx = int(banana[len(banana)-1])
#             message = ""
#             for i in range(len(banana)):
#                 if i == len(banana)-1:
#                     break
#                 message = message+banana[i]
#     except Exception:
#         print("no index given")


#     if(idx%5==3): # need to search for 2 pages   e.g. the index is 21-30 but one page only contains up to 25 books
#         reply_payload = []
#         title = []
#         code = []
#         media_id = []
        

#         # first half   21-25
#         pageid = int((idx-1)/5) +1 # Q U I C K   M A T H S 
#         pageid = pageid*2 - 1
#         try:
#             data = json.loads(search(message,pageid))
#         except Exception:
#             err(Reply_token)
#         cnt = 0
#         target = 25
#         try:
#             data['result'][0]
#         except KeyError:
#             nf(Reply_token,"multiple")
#             requests.post(notify_url, headers=notify_headers, data = {'message': 'NOT FOUND ' + message})
#             return 400
#         for item in data['result']:
#             if cnt < 20:
#                 cnt=cnt+1
#                 continue

#             print("{}   {} {} {}".format(cnt,item['title']['pretty'],item['id'],item['media_id']))
#             title.append(item['title']['pretty'])
#             code.append(item['id'])
#             media_id.append(item['media_id'])

#             cnt = cnt + 1
#             if cnt == target :
#                 break

#         # second half   26-30
#         pageid = pageid+1
#         try:
#             data = json.loads(search(message,pageid))
#         except Exception:
#             err(Reply_token)
#         cnt = 0
#         target = 5
#         for item in data['result']:
#             print("{}   {} {} {}".format(cnt,item['title']['pretty'],item['id'],item['media_id']))
#             title.append(item['title']['pretty'])
#             code.append(item['id'])
#             media_id.append(item['media_id'])

#             cnt = cnt + 1
#             if cnt == target :
#                 break
        



#     else:
#         pidx = (idx-1)/5+1   # Q U I C K   M A T H S     
#         pidx=pidx*2
#         if(idx <= 2):
#              pidx=pidx-1
#         try:
#             data = json.loads(search(message,pageid))
#         except Exception:
#             err(Reply_token)
            
#         try:
#             data['result'][0]
#         except KeyError:
#             nf(Reply_token,"multiple")
#             requests.post(notify_url, headers=notify_headers, data = {'message': 'NOT FOUND ' + message})
#             return 400
#         reply_payload,title,code,media_id = [],[],[],[]
#         cnt = 0
#         target = 10
#         if idx%5==2:
#             target = 20
#         elif idx%5==4:
#             target = 15
#         elif idx%5==0:
#             target=25
#         op = target-10 # 
#         for item in data['result']:
#             if cnt < op:
#                 cnt=cnt+1
#                 continue

#             print("{}   {} {} {}".format(cnt,item['title']['pretty'],item['id'],item['media_id']))
#             title.append(item['title']['pretty'])
#             code.append(item['id'])
#             media_id.append(item['media_id'])

#             cnt = cnt + 1
#             if cnt == target :
#                 break

    
#     for i in range(len(code)):
#         reply_payload.append( con(media_id[i], title[i], code[i])   )

#     if len(reply_payload) == 0:
#         print("not found!")
#     else:
#         LINE_API = 'https://api.line.me/v2/bot/message/reply'

#         Authorization = 'Bearer {}'.format(Channel_access_token)
#     #    print(reply_payload,indents=4)
#         headers = {
#             'Content-Type': 'application/json; charset=UTF-8',
#             'Authorization': Authorization
#         }

#         dt = {
#             "replyToken":Reply_token,
#             "messages":
#             [
#                 {
#                     "type": "flex",
#                     "altText": "Not safe for work",
#                     "contents": 
#                     {
#                         "type" : "carousel",
#                         "contents" : (reply_payload)
#                     }
#                 }
#             ]
#         }


#         dt = json.dumps(dt) # from dict to str
#         r = requests.post(LINE_API, headers=headers, data=dt) 
#         requests.post(notify_url, headers=notify_headers, data = {'message': message + " " + str(idx)})
#         print(r.text)
#         return 200

#bad code ชห ชื่อตัวแปรเบียวๆ

from bs4 import BeautifulSoup
import requests
import json
from modules.nhentai import search
from Project.Config import *


def multiple(payload):
    Reply_token = payload['events'][0]['replyToken']
    message = payload['events'][0]['message']['text']
    print(message)
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


    if(idx%5==3): # need to search for 2 pages   e.g. the index is 21-30 but one page only contains up to 25 books
        reply_payload = []
        title = []
        code = []
        media_id = []
        

        # first half   21-25
        pageid = int((idx-1)/5) +1 # Q U I C K   M A T H S 
        pageid = pageid*2 - 1
        try:
            data = json.loads(search(message,pageid))
        except Exception:
            err(Reply_token)
        cnt = 0
        target = 25
        try:
            data['data']['nhentai']['search']['result']
        except KeyError:
            nf(Reply_token,"multiple")
            requests.post(notify_url, headers=notify_headers, data = {'message': 'NOT FOUND ' + message})
            return 400
        for item in data['data']['nhentai']['search']['result']:
            if cnt < 20:
                cnt=cnt+1
                continue

            print("{}   {} {} {}".format(cnt,item['title']['pretty'],item['id'],item['media_id']))
            title.append(item['title']['pretty'])
            code.append(item['id'])
            media_id.append(item['media_id'])

            cnt = cnt + 1
            if cnt == target :
                break

        # second half   26-30
        pageid = pageid+1
        try:
            data = json.loads(search(message,pageid))
        except Exception:
            err(Reply_token)
        cnt = 0
        target = 5
        for item in data['data']['nhentai']['search']['result']:
            print("{}   {} {} {}".format(cnt,item['title']['pretty'],item['id'],item['media_id']))
            title.append(item['title']['pretty'])
            code.append(item['id'])
            media_id.append(item['media_id'])

            cnt = cnt + 1
            if cnt == target :
                break
        



    else:
        pidx = (idx-1)/5+1   # Q U I C K   M A T H S     
        pidx=pidx*2
        if(idx <= 2):
             pidx=pidx-1
        try:
            data = json.loads(search(message,pageid))
        except Exception:
            err(Reply_token)
            
        try:
            data['data']['nhentai']['search']['result']
        except KeyError:
            nf(Reply_token,"multiple")
            requests.post(notify_url, headers=notify_headers, data = {'message': 'NOT FOUND ' + message})
            return 400
        reply_payload,title,code,media_id = [],[],[],[]
        cnt = 0
        target = 10
        if idx%5==2:
            target = 20
        elif idx%5==4:
            target = 15
        elif idx%5==0:
            target=25
        op = target-10 # 
        for item in data['data']['nhentai']['search']['result']:
            if cnt < op:
                cnt=cnt+1
                continue

            print("{}   {} {} {}".format(cnt,item['title']['pretty'],item['id'],item['media_id']))
            title.append(item['title']['pretty'])
            code.append(item['id'])
            media_id.append(item['media_id'])

            cnt = cnt + 1
            if cnt == target :
                break

    
    for i in range(len(code)):
        reply_payload.append( con(media_id[i], title[i], code[i])   )

    if len(reply_payload) == 0:
        print("not found!")
    else:
        LINE_API = 'https://api.line.me/v2/bot/message/reply'

        Authorization = 'Bearer {}'.format(Channel_access_token)
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
        r = requests.post(LINE_API, headers=headers, data=dt) 
        requests.post(notify_url, headers=notify_headers, data = {'message': message + " " + str(idx)})
        print(r.text)
        return 200

