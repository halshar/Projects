import requests
import csv

from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top?ref_=ft_250'
r = requests.get(url)


def save_html(source, name):
    with open(name, 'wb') as f:
        f.write(source)

save_html(r.content, 'imdb_com')


with open('imdb_com', 'rb') as f:
    source = f.read()
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('imdb_scrape.csv', 'w')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Rank', 'Movie Name', 'Date of Release', 'Rating'])

    t_body = soup.find('tbody', class_='lister-list')
    rank = 1

    for tr in t_body.find_all('tr'):
        title = tr.find('td', class_='titleColumn').a.text
        print(title)

        date_of_release = tr.find('td', class_='titleColumn').span.text
        print(date_of_release)

        rating = tr.find('td', class_='ratingColumn imdbRating').strong.text
        print(rating)
        print('----------------------')
        csv_writer.writerow([rank, title, date_of_release, rating])
        rank += 1
    csv_file.close()
