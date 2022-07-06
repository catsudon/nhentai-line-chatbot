import requests,json

def search(query="แนะนำ",page=1):
    if not "แนะนำ" in query and query != "/":
        url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=popular"
    else:
        url = f"https://nhentai.net/api/galleries/search?sort=popular&query=uploaded:<2d"

    res = requests.get(url).content.decode()
    return res

def getBookById(_id):
    if _id == None:
        return "id required."
    url = 'https://api.hifumin.app/v1/graphql'
    query = '{nhentai {  by(id:'+str(_id)+', channel:"HIFUMIN_FIRST")  {    id    mediaId    title {display:pretty}    images {cover {t,w,h}}  }}}'
    
    r = requests.post(url, json={'query':query})
    print(r.status_code, r.text)
    res = json.loads(r)
    return res
    
if __name__ == "__main__":
    print(getBookById(245031))
