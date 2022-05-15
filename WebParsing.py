import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

page = 1
while page < 29:
    url = 'https://tortuga.ge/collections/samagido-tamashebi?page=' + str(page)
    response = requests.get(url)
    # print(response.status_code)

    file = open('board_games.csv', "w", encoding='UTF-8_sig')
    header = 'დასახელება,მწარმოებელი,ფასი,მარაგი\n'
    file.write(header)

    content = response.text
    # print(content)

    soup = BeautifulSoup(content, 'html.parser')
    div = soup.find('div', {'class': 'product-list product-list--collection product-list--with-sidebar'})
    print(soup.title.text)
    board_games = div.find_all('div', {'class': 'product-item__info'})
    # print(board_games)
    for each in board_games:
        game = each.a.text
        price = each.span.text
        name = each.find('a', class_='product-item__title text--strong link').text
        stock = each.button.text
        print(game, price, name, stock)
        file.write(name + ',' + game + ',' + price + ',' + stock + '\n')

    page += 13
    sleep(randint(7, 21))
