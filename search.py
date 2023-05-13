import requests
from bs4 import BeautifulSoup

def search_google_images(search_term):
    url = f"https://www.google.com/search?q={search_term}&source=lnms&tbm=isch"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    image_links = []
    for img in soup.find_all("img")[:10]:
        link = img.get("src")
        if link and "http" in link and not link.startswith("data:"):
            image_links.append(link)
    return image_links


search_term = "cute puppies"
image_links = search_google_images(search_term)
print(image_links)
