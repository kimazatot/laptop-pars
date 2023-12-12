import requests
from bs4 import BeautifulSoup
import csv


def write_to_csv(data: dict):
    with open('data.csv', 'a') as file:
        write = csv.writer(file)
        write.writerow((data['title'], data['price'], data['img'], data['desc']))



def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text)
    # return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    cars = soup.find('div', class_='catalog-list').find_all('a')
    # print(cars)
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title = ''
        # print(title)
        # print(car)
        # print('=====================')

        try:
            price = car.find('span', class_='catalog-item-price').text.strip()
        except:
            price = ''
        # print(price)

# try:
#     price = car.find('span', class_='catalog-item-price').text
# except:
#     price = ''

        try:
            desc = car.find('span', class_='catalog-item-descr').text.split()
            desca = ' '.join(desc)
        except:
            desca = ''
        
        # print(desc)

        try:
            img = car.find('img').get('src')
        except:
            img = ''
        # print(img)


