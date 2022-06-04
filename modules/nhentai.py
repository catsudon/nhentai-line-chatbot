# import requests,json
# import time
# def search(query=None,page=1):
#     if query is not None:
#         url = f"https://nhentai.net/api/galleries/search?query={query}&page={page}&sort=popular"
#     else:
#         url = f"https://nhentai.net/api/galleries/all?page={page}&sort=popular"
#     requests.get(url)
#     time.sleep(1)
#     requests.get(url)
#     res = requests.get(url).content.decode()
#     return res

# def getBookById(_id):
#     if _id == None:
#         return "id required."
#     url = f"https://nhentai.net/api/gallery/{_id}"
    
#     requests.get(url)
#     time.sleep(1)
#     requests.get(url)
#     res = requests.get(url).content.decode()
#     return res

# if __name__ == "__main__":
#     print(getBookById(245031))

import requests,json
import time
from bs4 import BeautifulSoup

def search(query="home",page=1):
    if query is not "home":
        url = f"https://hentaifox.com/search/?q={query}&sort=popular&page={page}"
    else:
        url = "https://hentaifox.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    divs = soup.find_all("div", {"class": "thumb"})
    books = []
    for div in divs:
        cover = div.find_all('img')[0]['src']
        title = div.find_all('h2')[0].text.strip()
        code  = div.find_all('a')[2]['href']
        books.append({
                "cover_url" : cover,
                "title" : title,
                "code" : code
            })
        
   # print(books)
    return books


def getBookById(_id):
    if _id == None:
        return "id required."
    url = f"https://nhentai.net/api/gallery/{_id}"
    url = f"https://nhentai.to/g/{_id}"
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    img = soup.find_all('img')[1]
    
    book = {
        "cover_url" : img['src'],
        "title" : soup.find_all('h1')[0].text.strip(),
        "code" : _id
    }
    return book

if __name__ == "__main__":
    print(getBookById(245031))