Channel_secret= '896f339609b844d5f6fefa54e8622378'
Channel_access_token = 'kitU7r1CNHa1+t4eUACoTRonmtZdX+c2SSTGW7Hs2Zmu+R8WK88kl8etpaxTGE3inWBxZUxa7gJ/kjjqJTCcOnaebc2AXY1ixendrmH436NjMpSLYSVm4+BVgOsTfIEQdnvyo+OAEcKo2nSq6O+i5gdB04t89/1O/w1cDnyilFU='

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