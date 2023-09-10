import requests
import csv
from bs4 import BeautifulSoup
from json import loads as json_loads

page = requests.get("https://www.adinehbook.com/gp/browse?node=d400")
bs = BeautifulSoup(page.text, "html.parser")
data = bs.find_all(class_="item contrast_font product-layout")

file = open("adinehbook.csv",'w',newline='',encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["name",'author','price'])
big_list=[]
for simple_data in data:
    try:
        csv_lst=[]
        name = simple_data.find_all_next(class_="name")[0].text.strip()
        author = simple_data.find_all_next(class_="right")[0].find_next(class_="by_string main_font").text.strip()
        price = simple_data.find_all_next(class_='price')[0].find_next(class_='price-old').text.strip()

        csv_lst.append(str(name))
        csv_lst.append(str(author))
        csv_lst.append(str(price))
        big_list.append(csv_lst)

    except:
        continue
writer.writerows(big_list)

