import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent


url = "https://kups.club/"
headers = {"user-agent": fake_useragent.UserAgent().random}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
products = soup.find_all("div", class_="row mt-4")
for product in products:
    title_products = product.find("h3", class_="card-title")
    print(title_products.text)
