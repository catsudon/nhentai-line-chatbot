import requests,json
import time
from bs4 import BeautifulSoup

def search(query=None,page=1):
    if query is not None:
        url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=popular"
    else:
        url = f"https://nhentai.net/api/galleries/all?page={page}&sort=popular"
    requests.get(url)
    time.sleep(1)
    requests.get(url)
    res = requests.get(url).content.decode()
    return res

def getBookById(_id):
    if _id == None:
        return "id required."
    url = f"https://nhentai.net/api/gallery/{_id}"
    url = f"https://hifumin.app/h/{_id}"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    img = soup.find_all('img')[0]
    
    book = {
        "cover_url" : img['src'],
        "title" : soup.find_all('h1')[0].text.strip(),
        "code" : _id
    }
    return book

if __name__ == "__main__":
    print(getBookById(245031))