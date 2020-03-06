# Word Cloud Parlamentar

A ideia desse projeto é mostrar, de forma agrádavel, quais foram as palavras mais utilizadas pelos deputados federais 
em seus discursos na Câmara Federal no ano de 2019. 

## Início

Ao baixar/clonar o repositório certifique-se de que as bibliotecas necessárias estão instaladas e o ambiente está
pronto. Depois basta rodar o script makeWordCloud.py, a imagem com o word cloud será gerada como  wordcloudBR.png

### Prerequisitos

Para que o script funcione corretamente são necessárias, além de um interpretador python 3, as seguintes bibliotecas:

* [bs4 4.8.2](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [requests 2.23.0](https://requests.readthedocs.io/en/master/)
* [asyncio 3.4.3](https://docs.python.org/3/library/asyncio.html)
* [aiohttp 3.6.2](https://docs.aiohttp.org/en/stable/)
* [matplotlib 3.1.3](https://matplotlib.org/)
* [numpy 1.18.1](https://numpy.org/)
* [wordcloud 1.6.0](http://amueller.github.io/word_cloud/index.html)

Caso essas bibliotecas não estejam instaladas, é possivel instala-las usando o comando:
```
pip3 install biblioteca
```

### Gerando o word cloud parlamentar 

Para gerar o word cloud parlamentar basta rodar o seguinte comando:
```
python3 makeWordCloud.py
```
## Versão

Esta é primeira versão do projeto, acompanhe a evolução do projeto [aqui](https://github.com/gui-lourenco/WordCloud/). 

## Autor

* **Guilherme Guimarães**
