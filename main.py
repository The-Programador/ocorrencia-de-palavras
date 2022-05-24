'''
Algoritmo que analisa e define quais são as 10 palavras mais recorrentes em um arquivo de texto, plotando um gráfico matplotlib.

Sinta-se a vontade para modificar e evoluir, corrigir eventuais erros de lógica! 
'''
#módulos necessários para o funcionamento correto da aplicação
from nltk.corpus import stopwords
import matplotlib.pyplot as pt
import re

stop = stopwords.words('english')

def clearWords(textTemp):
	'''
	função para fazer a limpeza do texto passado para o parâmetro "texTemp"
	param textTemp: Texto "Bruto"
	return: Texto tratado
	'''
    textTemp = re.sub("[^\w\s\-']", ' ', textTemp).lower()
    textTemp = re.sub('\d', '', textTemp)
    textTemp = re.sub('\s+', ' ', textTemp)
    return textTemp

def extractWords(wordList):
	'''
	devolve uma lista de palavras filtradas (Que não são stopwords, ou palavras de sintaxe comum, conectivos lógicos)
	param wordList: Texto tratado para extração de palavras, e inserção em uma lista
	return: Lista de palavras filtradas
	'''
    newWordList = []
    for word in wordList:
        if word not in stop:
            newWordList.append(word)
    return newWordList


def enumerateWords(wordList):
	'''
	define a lista em uma lista de dicionários ordenada por número de ocorrências e devolve a mesma.
	param wordList: lista de palavras filtradas
	return: Lista de Ocorrências 
	'''
    occurrence = {}
    for word in wordList:
        if word in occurrence:
            occurrence[word] += 1
        else:
            occurrence[word] = 1
    return occurrence

try:
    with open('texto5.txt', encoding='utf-8') as text:
        pass
except FileNotFoundError:
    print('Arquivo não Encontrado!!!')
else:
    with open('texto5.txt', encoding='utf-8') as text:
        textAll = text.read().replace('\n', ' ')
        wordList = extractWords(clearWords(textAll).split(' '))
        relation = enumerateWords(wordList)
        relation = list(relation.items())

        relation.sort(key=lambda i: i[1], reverse=True)

        print(relation[:10])

        x, y = zip(*(relation[:10]))

        figure, axis = pt.subplots()
        pt.ylabel('Quantidade de Vezes')
        pt.xlabel('Termos Ranqueados')
        pt.title('Termos mais recorrentes no Texto')
        axis.bar(x, y, width=0.7, edgecolor='white', color='red', linewidth=0.1)
        pt.xticks(rotation=45)
        pt.show()
