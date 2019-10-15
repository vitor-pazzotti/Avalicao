#!/usr/bin/env python3.7

import requests
from datetime import datetime
import csv
import os
import time

# função para localizar e extrair o titulo da moeda 
cwd = os.getcwd()
def moeda(html):
	"""paramatro: html -> conteúdo da páginareturn: conteduo -> tipo de moeda"""
	#verifica o titulo da moeda
	aux = html.find("instrumentH1inlineblock") + 30
	#coloca o titulo em um formato sem espaços
	tipo_moeda = html[aux:aux+31]

	#retorna o bloco de código como tipo_moeda
	return tipo_moeda

def cotacao(html):
	#localiza cotacao
	aux = html.find("lastInst pid-2103-last") + 30
	#retira os espacos do valor obtido
	cot = html[aux:aux+29].strip()

#retorno da função cotacao
	return cot

def mudanca(html):
	#localiza mudanca
	aux = html.find("pid-2103-pc") + 30
	#retira os espaços da variavel
	mud = html[aux:aux+20].strip()

	return mud

def percentual(html):
	#localiza percentual
	aux = html.find("pid-2103-pcp") + 30
	#retira os espaços da variavel
	perc = html[aux:aux+10].strip()

	return perc

def data(r):
	#localiza a data e retira GMT
	aux = r.headers["date"][:-4]
	#formatação da data para atender o exercicio
	date = datetime.strptime(aux, '%a, %d %b %Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')

	return date

def gravar(saida):
	#abertura do arquivo com append
        #Mudei a abertura do arquivo para um context manager.
	h = time.time()
	with open( cwd + f'/vitorPazzotti/crawler_dolar/dolar_{h}.csv', 'a+') as f:
            writer = csv.writer(f, delimiter = ',')
	#verifica se o arquivo está vazio, e se estiver, escreve o cabeçalho.
	if os.stat(cwd + f'/vitorPazzotti/crawler_dolar/dolar_{h}.csv').st_size == 0:
		writer.writerow(['Currency', 'Value', 'Change', 'Percentual', 'Timestamp'])

	writer.writerow(saida)

if __name__ == '__main__':
    # Mudança para capturar 20 vezes a mesma moeda.
    for i in range(20):
	# estabelece conexão com a url
        r = requests.get(url="https://m.investing.com/currencies/usd-brl", headers={'User-Agent':'curl/7.52.1'})
	#r.text -> html todo
        html = r.text
	#armazena as variaveis em uma linha
        saida = [moeda(html), cotacao(html), mudanca(html),
		percentual(html), data(r)]

	#chamada do metodo para armazenar no arquivo
        gravar(saida)
        

