# enlace original https://books.toscrape.com/catalogue/page-2.html
import bs4
import requests

# main url
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

print("scraping.... please wait...")
# iterar paginas de la 1 a la 50
for num_pagina in range(1, 21):

    # crear urls
    url_pagina = url_base.format(num_pagina)
    pagina_raw = requests.get(url_pagina)
    site = bs4.BeautifulSoup(pagina_raw.text, "lxml")

    # seleccionar libros
    books = site.select('.product_pod')

    # iteramos en cada uno de los libros
    for book in books:

        # libros que tengas un rating de 4 o 5 estrellas
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            # guardamos titulo
            title_book = book.select("a")[1]['title']

            # agregar el libro a la lista
            titulos_rating_alto.append(title_book)


print("Finish scraping :)\nEstos son los siguientes títulos que he encontrado: ")

# libros totales
for t in titulos_rating_alto:
    print(t)

