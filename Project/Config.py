Channel_access_token = 'YOUR LINE ACCESS TOKEN HERE'

def con(code,title,pic,w=350,h=500):
    return {
    "type": "bubble",
    "direction": "ltr",
    "hero": {
      "type": "image",
      "url": "https://t.nhentai.net/galleries/{}/thumb.jpg".format(pic),
      "size": "full",
      "aspectRatio": "{}:{}".format(w,h),
      "aspectMode": "fit",
      "backgroundColor": "#6A0707"
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": title[0:41],
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
            "uri": "https://nhentai.net/g/"+str(code)
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