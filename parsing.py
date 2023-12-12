import requests
from bs4 import BeautifulSoup as bs 
import csv

def write_to_csv(data):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img'], data['artic']])

def get_data(html):
    soup = bs(html, 'html.parser')
    product_list = soup.find_all('div', class_='row')
    
    for product in product_list:
        title = product.find('div', class_='rows').find('a').text.strip()
        price = product.find('span', class_='price').text.strip()
        img = product.find('a', class_='product-image-link').find('img')['src']
        img = 'https://enter.kg' + img
        artic = product.find('span', class_='sku').text.strip()
        
        data = {
            'title': title,
            'price': price,
            'img': img,
            'artic': artic
        }
        write_to_csv(data)

def main():
    base_url = 'https://enter.kg/computers/noutbuki_bishkek?page='
    page = 1

    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['title', 'price', 'image', 'article'])

    while True:
        url = base_url + str(page)
        html = requests.get(url).text
        get_data(html)
        page += 1
        
        # soup = bs(html, 'html.parser')
        # next_button = soup.find('li', class_='pagination-next')
        # if not next_button:   #парсинг до конца
        #     break


main()
