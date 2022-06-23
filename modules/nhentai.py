import requests,json

def search(query="แนะนำ",page=1):
    if not "แนะนำ" in query and query is not "/":
        url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=popular"
    else:
        url = f"https://nhentai.net/api/galleries/search?sort=popular&uploaded%3C1d&query=/&page={page}"

    res = requests.get(url).content.decode()
    return res

def getBookById(_id):
    if _id == None:
        return "id required."
    url = f"https://nhentai.net/api/gallery/{_id}"
    
    res = json.loads(requests.get(url).content.decode())
    return res

if __name__ == "__main__":
    print(getBookById(245031))
