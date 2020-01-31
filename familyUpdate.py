import requests
from bs4 import BeautifulSoup

dominioFamily = requests.get("http://download.dominiosistemas.com.br/atualizacao/contabil/")
dominioUpdateC = requests.get("http://download.dominiosistemas.com.br/atualizacao/contabil/101c01/atualizacoes/")
#list(body.children)

soup = BeautifulSoup(dominioFamily.content, 'html.parser')
#retornando conteudo e o html da pagina
soupUpdate = BeautifulSoup(dominioUpdateC.content, 'html.parser')

list(soup.children)
#listando tudo em modo organizado, perto ao paragrafo

list(soupUpdate.children)

pagina = soup.find_all('a')
#encontrando tudo que cita a tag a

paginaUpdate = soupUpdate.find_all('a')

print(pagina,paginaUpdate)