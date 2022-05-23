import requests,json
import time
from bs4 import BeautifulSoup

def search(query="home",page=1):
    if query is not "home":
        url = f"https://nhentai.to/search?q={query}&page={page}"
    else:
        url = "https://nhentai.to/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    divs = soup.find_all("div", {"class": "gallery"})
    
    for div in divs:
        cover = div.find_all('a')[0].find_all('img')[1]['src']
        title = div.find_all('div')[0].text.strip()
        code  = div.find_all('a')[0]['href'].replace('/','').replace('g','')
        books.append({
                "cover_url" : cover,
                "title" : title,
                "code" : code
            })
    books = []
    return books
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