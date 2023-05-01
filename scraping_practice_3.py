import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

url = 'https://scraping-for-beginner.herokuapp.com/image'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
img_tag = soup.find('img')
img_tag['src']

root_url = 'https://scraping-for-beginner.herokuapp.com'
img_url = root_url + img_tag['src']

img = Image.open(io.BytesIO(requests.get(img_url).content))
img.save('img/sample.jpg')
