import requests
import json


Channel_access_token = 'CHANNEL ACCESS TOKEN'


notify_url = 'https://notify-api.line.me/api/notify'
notify_token = 'NOTIFY TOKEN'
notify_headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+notify_token}


def log(code, title):
    requests.post(notify_url, headers=notify_headers, data = {'message': str(code) + " : " + title + "\n      https://nhentai.net/g/"+str(code)})

def con(img, title, code, w=350, h=500):
      
    return {
    "type": "bubble",
    "size": "mega",
    "direction": "ltr",
    "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": title[0:41],
        "weight": "regular",
        "size": "lg",
        "color": "#3E2929",
        "contents": []
      }]
    },
    "hero": {
      "type": "image",
      "url": "https://t.nhentai.net/galleries/{}/thumb.jpg".format(img),
      "size": "full",
      "aspectMode": "cover",
      "aspectRatio": "{}:{}".format(w, h),
      "backgroundColor": "#FFFFFFFF"
    },
    "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "spacer",
        "size": "md"
      }
    ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        
        
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          
          {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "READ",
            "uri": "https://nhentai.net/g/"+str(code)+"/1"
          },
          "flex": 6,
          "color": "#ff5e87",
          "margin": "xs",
          "height": "md",
          "style": "primary",
          "gravity": "top"
        }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
         
          {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "READ (no ads)",
            "uri": "https://hifumin.app/h/"+str(code)+"/1"
          },
          "flex": 6,
          "color": "#9564f5",
          "margin": "xs",
          "height": "md",
          "style": "primary",
          "gravity": "top"
        }
        ]
      },
        

        
        
      #   ,
      #   {
      #   "type": "button",
      #   "action": {
      #     "type": "postback",
      #     "label": "PREVIEW",
      #     "text": "@p {}".format(str(code)),
      #     "data": "view preview"
      #   },
      #   "flex": 6,
      #   "color": "#9564f5",
      #   "margin": "xs",
      #   "height": "md",
      #   "style": "primary",
      #   "gravity": "top"
      # }
      ]
    }
  }


def con2(img, title, code, w=350, h=500):
      
    return {
    "type": "bubble",
    "size": "mega",
    "direction": "ltr",
    "header": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": title[0:41],
        "weight": "regular",
        "size": "lg",
        "color": "#3E2929",
        "contents": []
      }]
    },
    "hero": {
      "type": "image",
      "url": "https://t.nhentai.net/galleries/{}/thumb.jpg".format(img),
      "size": "full",
      "aspectMode": "cover",
      "aspectRatio": "{}:{}".format(w, h),
      "backgroundColor": "#FFFFFFFF"
    },
    "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "spacer",
        "size": "md"
      }
    ]
    },
    "footer": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        
        
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          
          {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "READ",
            "uri": "https://nhentai.net/g/"+str(code)+"/1"
          },
          "flex": 6,
          "color": "#ff5e87",
          "margin": "xs",
          "height": "md",
          "style": "primary",
          "gravity": "top"
        }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
         
          {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "READ (no ads)",
            "uri": "https://hifumin.app/h/"+str(code)+"/1"
          },
          "flex": 6,
          "color": "#9564f5",
          "margin": "xs",
          "height": "md",
          "style": "primary",
          "gravity": "top"
        }
        ]
      },
        

        
        
      #   ,
      #   {
      #   "type": "button",
      #   "action": {
      #     "type": "postback",
      #     "label": "PREVIEW",
      #     "text": "@p {}".format(str(code)),
      #     "data": "view preview"
      #   },
      #   "flex": 6,
      #   "color": "#9564f5",
      #   "margin": "xs",
      #   "height": "md",
      #   "style": "primary",
      #   "gravity": "top"
      # }
      ]
    }
  }

def con3(sauce,w=350,h=500):
    return {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
      "type": "image",
      "url": sauce,
      "size": "full",
      "aspectRatio": "{}:{}".format(w,h),
      "aspectMode": "fit",
      "backgroundColor": "#FFC0CB"
    }
  }


def nf(Reply_token,type = "index"):
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
              "type": "text",
              "text": "not found!"
          }
      ]
  }


  dt = json.dumps(dt) # from dict to str
  r = requests.post(LINE_API, headers=headers, data=dt) 
  print(type)
  print("search not found")
  return 200