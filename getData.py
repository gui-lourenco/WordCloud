# Libs and frameworks
from bs4 import BeautifulSoup
import requests as req
import asyncio as asy
import aiohttp as aio
import json
import pickle as pk

def text_organize(discurses):
    res = []
    for discurse in discurses:
        try:
            text = json.loads(discurse.find('p').text)
            text = text['dados'][0]['transcricao']
            res.append(text)
        
        except:
            continue
        
    return res


async def get_info(url, session, *args):
    url = url.format(*args)
    async with session.get(url) as info:
        info = BeautifulSoup(await info.text(), 'lxml')
        return info

async def get_discurse(congressmen):
    connector = aio.TCPConnector(limit=10) # Número de conexões
    timeout = aio.ClientTimeout(total=60*60) # Tempo máximo de espera por resposta

    async with aio.ClientSession(trust_env=True, timeout=timeout, connector=connector) as session:
        URL = 'https://dadosabertos.camara.leg.br/api/v2/deputados/{}/discursos?dataInicio=2019-01-01&dataFim=2019-12-31&ordenarPor=dataHoraInicio&ordem=ASC'
        discurses = [get_info(URL, session, c) for c in congressmen]
        return text_organize(await asy.gather(*discurses))

def get_text():
    # Get all 2019 congressman id 
    congressmen = req.get("https://dadosabertos.camara.leg.br/api/v2/deputados?dataInicio=2019-01-01&dataFim=2019-12-31&ordem=ASC&ordenarPor=nome")
    congressmen = BeautifulSoup(congressmen.text, 'html.parser')    
    congressmen = json.loads(congressmen.prettify())['dados'] 

    # Get all discurses on Câmara Federal in 2019
    loop = asy.get_event_loop()
    res = loop.run_until_complete(get_discurse([data['id'] for data in congressmen]))
    loop.close()

    # Save texts in a serial file 'text.p'
    pk.dump(res, open('text.p', 'wb'))