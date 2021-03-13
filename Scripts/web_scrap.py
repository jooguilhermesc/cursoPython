#Importa bibliotecas
import requests
from bs4 import BeautifulSoup

#Define a URL que vamos utilizar
url = 'https://www.aosfatos.org/noticias/investigamos/?page=1'

#Acessa a URL definida
"""
ERRO NO CÓDIGO COM BS4 QUANDO NÃO USA "TEXT"
"""
html = requests.get(url)

#Acessa o HTML da URL definida
bs = BeautifulSoup(html.content,'html.parser')

#Procura por todos os elementos que desejamos nesse HTML
print(bs.title.text)

#Retorna todos os elementos
link = bs.find('a', class_='entry-card infinite-item')
print(link.text)
print(link.get('href'))

#Armazena todos os elementos em formato .CSV