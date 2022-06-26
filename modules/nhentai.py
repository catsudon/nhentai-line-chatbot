import requests,json

def search(query="แนะนำ",page=1):
    if not "แนะนำ" in query and query is not "/":
        url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=popular"
    else:
        url = f"https://nhentai.net/api/galleries/search?sort=popular&query=uploaded:<2d"

    res = requests.get(url).content.decode()
    return res

def getBookById(_id):
    if _id == None:
        return "id required."
    url = f"https://nhentai.net/api/gallery/{_id}"
    query = '{nhentai {  by(id:'+str(_id)+', channel:"HIFUMIN_FIRST")  {    id    mediaId    title {display:pretty}    images {cover {t,w,h}}  }}}'
    
    res = json.loads(requests.post(url, json={'query':query}).text)
    return res

if __name__ == "__main__":
    print(getBookById(245031))
