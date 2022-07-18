import requests,json

def search(query="แนะนำ",page=1):
    if not "แนะนำ" in query and query != "/":
        query = '{nhentai {\n  search(with:"' + str(query) + '", channel:"HIFUMIN_FIRST")\n  {\n    result {      id      mediaId      title {\n        pretty}}}}}'
    else:
        query = '{nhentai {\n  search(with:"", channel:"HIFUMIN_FIRST")\n  {\n    result {\n      id\n      mediaId\n      title {\n        pretty\n      }\n      \n    }\n  }\n}\n}'
    
    url = "https://api.hifumin.app/v1/graphql"
    r = requests.post(url, json={'query':query})
    return json.loads(r.text)

def getBookById(_id):
    if _id == None:
        return "id required."
    url = 'https://api.hifumin.app/v1/graphql'
    query = '{nhentai {  by(id:'+str(_id)+', channel:"HIFUMIN_FIRST")  {    id    mediaId    title {display:pretty}    images {cover {t,w,h}}  }}}'
    
    r = requests.post(url, json={'query':query})
    print(r.status_code, r.text)
    res = json.loads(r.text)
    return res
    
if __name__ == "__main__":
    idx=1
    pidx = (idx-1)/5+1   # Q U I C K   M A T H S     
    pidx=pidx*2
    if(idx <= 2):
         pidx=pidx-1
    
        
    try:
        books = json.loads(search("asdjsajwek234asjd",pidx))
        
    except Exception :
        pass
    for item in books['data']['nhentai']['search']['result']:
        print(item)