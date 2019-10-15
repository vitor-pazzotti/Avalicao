#! /usr/bin/env python3

from os import stat
import os
from bs4 import BeautifulSoup
from csv import writer
from datetime import datetime
import requests
import time

# endereço do site que será raspado
# URL
cwd = os.getcwd()
crypto_Url = "https://m.investing.com/crypto/"

requestString = requests.get(url = crypto_Url, headers = {'User-Agent':'curl/7.52.1'})
soup = BeautifulSoup(requestString.text, "html.parser") #Troquei o parser para html.parser

# Faz o scrap do objeto soup que contém o html do site

content = soup.findAll('tr')

#formata a data para nosso horario

date = datetime.strptime(requestString.headers['Date'][:-4], '%a, %d %b %Y %H:%M:%S')

#Adicionei um context manager
#Cria o arquivo CSV.:
h = time.time()
with open(cwd + f"/vitorPazzotti/crawler_crypto/crypto_{h}.csv", "a+") as f:
    writers = writer(f, delimiter = ",")
    #Verifica se o arquivo está vazio, e escreve o cabeçalho.
    if stat(cwd + f"/vitorPazzotti/crawler_crypto/crypto_{h}.csv").st_size == 0:
        writers.writerow(["#", "Name", "Price(USD)", "Chg(24H)", "Var(7D)", "Symbol", "Price(BTC)", "MarketCap", "Vol(24H)", "Total Volume", "Timestamp"])

    """
    Laço utilizado para formatar e inserir os valores no arquivo csv.
    As linhas estão dispostas conforme os valores das colunas e sua data formatada
    """
    for c in content[1:]:
        l = c.get_text().replace('\t', '').split('\n')
        L = list(filter(None, l))

        writers.writerow([L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8],L[9], date])


