#!/usr/bin/env python
# coding: utf-8

import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import csv
import nltk
from datetime import datetime
from urllib import request
from nltk.tokenize import word_tokenize
import numpy as np

print('')
print("Bem vindo ao raspador de dados do Twitter!!\n")

texto = str(input('o que voce quer pesquisar?:'))
data1= input('Do dia (yyyy-mm-dd):')
data2 = input('até dia (yyyy-mm-dd):')

try:
    # while true é no final pq essa é a primeira passagem
    # na segunda que gera o looping
    while True:
        if datetime.strptime(data1, '%Y-%m-%d') and datetime.strptime(data2, '%Y-%m-%d'):
            print(True)
            teclado = "{} since:{} until:{}".format(texto, data1, data2)
            maxTweets = 3000
            i = 0
            tweets_list = []

            for tweet in sntwitter.TwitterSearchScraper(teclado).get_items():
                if i > maxTweets:
                    break
                tweets_list.append([tweet.date, tweet.url, tweet.username, tweet.content])
                i = i + 1

            tweets_df = pd.DataFrame(tweets_list, columns=['date', 'url', 'username', 'content'])
            nltk.download('punkt')
            nltk.download('stopwords')

            stop_words = nltk.corpus.stopwords.words('portuguese')
            stop_words = stop_words + list(
                [',', '.', 'https', ':', '!', '#', '@', '?', '/', 'O', 'vai', '|', '–', 'pra', 'a', 'e', '-'])


            def remove_stopwords(x):
                word_tokens = nltk.word_tokenize(x)
                # print(word_tokens)
                filtered_sentence = ' '.join([w for w in word_tokens if not (w in stop_words or len(w) < 4)])
                return filtered_sentence


            tweets_df['filtered_text'] = tweets_df['content'].apply(lambda x: remove_stopwords(x))

            text_count = pd.Series(' '.join(tweets_df['filtered_text'].str.lower()).split()).value_counts()[:20]

            print(tweets_df.head())

            save = input("deseja salvar o arquivo ? s/n:")

            if save == 's' or save == 'S' or save == 'Sim' or save == "sim":
                nome_arquivo = input("Nome do arquivo:")
                tweets_df.to_csv('{}.csv'.format(nome_arquivo), sep=';', encoding='utf-8-sig', index=False)
                print('\n')
                print('Raspagem feita com sucesso!!\n')
                break

            elif save == 'n' or save == 'N' or save == 'Não' or save == 'não':
                print('\n')
                print('obrigado por usar nossa API\n')
                break

            # Colocar Regex para filtrar o link e baixar

            # Validate URL
            # url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
            # re.match(url_pattern, 'https://uibakery.io') # Returns Match object
            # re.match(url_pattern, 'https:/uibakery.io') # Returns None
            #
            # # Extract URL from a string
            # "((http | https)\:\ / \ /)?[a - zA - Z0 - 9\.\ / \?\:@\-_ =  # ]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
            # url_extract_pattern = "https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)"
            # re.findall(url_extract_pattern, 'You can view more details at https://uibakery.io or just ping via email.') # returns ['https://uibakery.io']
            #
            # file_url = 'https://www.site.com/meuarquivo.txt'
            #
            # file = 'arquivolocal.txt'
            #
            # request.urlretrieve(file_url , file )

except ValueError:
        print('end')


"""
INSERÇÃO NO BANCO DE DADOS DO MYSQL A CADA EXECUÇÃO DO CODIGO 
"""
import mysql.connector as sql

from mysql.connector import Error 

conexao = sql.connect( host ="localhost",
                     user = "root",
                     port = 3306,
                     database= 'db_consult',
                     password= 'admin')

if conexao.is_connected():

    db_info = conexao.get_server_info()

    print('Conectado ao servidor MySQL versão',db_info)

    cursor = conexao.cursor()

    cursor.execute("select database();")

    linha= cursor.fetchone()

    print("Conectado ao banco de dados", linha)

try:

    table = """ CREATE TABLE Candidatos (
                Email VARCHAR(255) NOT NULL,
                First_Name CHAR(25) NOT NULL,
                Last_Name CHAR(25),
                Score INT
            ); """
    
    cursor.execute(table)

    conexao.commit()

    print(table)

    cursor.close()

except Error as erro:
    
    print("Falha ao inserir os dados no MYSQL: {}".format(erro))

finally:
    
    if conexao.is_connected():

       conexao.close()

       print("A Conexão ao MySQL foi encerrada")


