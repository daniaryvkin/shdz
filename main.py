import requests
from bs4 import BeautifulSoup
import lxml
import fake_useragent


url = "https://allo.ua/ua/roboty-pylesosy/"
headers = {"user-agent": fake_useragent.UserAgent().random}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
products = soup.find_all("div", class_="product-card")
for product in products:
    title_products = product.find("a", class_="product-card__title")
    old_products = product.find("span", class_="sum")
    print(title_products.text)
    print(old_products.text)
    a = open("po.txt", "a")
    a.write(title_products.text)
    a.write("     ")
    a.write(old_products.text)
    a.write("     ")
    try:
        new_products = product.find("div", class_="v-pb__cur discount")
        print(new_products.text)
        print()
        a = open("po.txt", "a")
        a.write(new_products.text)
        a.write("     ")

    except BaseException:
        print(title_products.text)
        print(old_products.text)
        print("Скидки нету")
        print()
        a = open("po.txt", "a")
        a.write(old_products.text)
        a.write("Скидки нету")
        a.write("     ")

a.close()