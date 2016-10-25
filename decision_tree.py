#!/usr/bin/env python
#encoding:utf8

import sys
import csv
import math
import os

class NoArvore:
    def __init__(self, atributo, positivo, negativo):
        self.atributo = atributo
        self.positivo = positivo
        self.negativo = negativo

    def imprime(self):
        print
        print "(",self.atributo,")[", self.positivo , "P, " , self.negativo , "N]"

    def calc_unidade_entropia(self, valor):
        return (valor)*math.log(valor, 2)

    def calcula_entropia(self):
        denominador = float(self.positivo) + float(self.negativo)
        valor_positivo = self.positivo/denominador
        valor_negativo = self.negativo/denominador
        entropia = -self.calc_unidade_entropia(valor_positivo) - self.calc_unidade_entropia(valor_negativo)
        return entropia

#Teste da classe
novo = NoArvore("raiz",2,3)
novo.imprime()

def calc_unidade_entropia(valor):
    return (valor)*math.log(valor, 2)

def calcula_entropia(positivo, negativo):
    denominador = positivo + negativo
    valor_positivo = positivo/denominador
    valor_negativo = negativo/denominador
    entropia = -calc_unidade_entropia(valor_positivo) - calc_unidade_entropia(valor_negativo)
    return entropia
#Teste do cálculo da entropia
print calcula_entropia(9.0 , 5.0)


#Carrega linhas de um arquivo CSV para um arquivo destino com exceção da última
#coluna
def carrega_csv(csv_filename, arrayDestino):
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0: continue
            arrayDestino.append(r)
    f.close()

baseDeDados = []
carrega_csv('iris.csv',baseDeDados)

def cria_no_inicial(baseDeDados, atributoPositivo):
    positivo = 0
    negativo = 0
    for item in baseDeDados:
        if item[len(item)-1] == atributoPositivo:
            positivo += 1
        else:
            negativo += 1

    print "postivo", positivo
    print "negativo", negativo
    return NoArvore(atributoPositivo,positivo,negativo)

def cria_no_raiz(lista_de_nos):
    maior_entropia = 0

    for no in lista_de_nos:
        if no.calcula_entropia() > maior_entropia:
            raiz = no
            maior_entropia = no.calcula_entropia()

    print "No raiz", raiz.imprime()



setosa = cria_no_inicial(baseDeDados, 'setosa')
versicolor = cria_no_inicial(baseDeDados, 'versicolor')
virginica = cria_no_inicial(baseDeDados, 'virginica')
os.system('clear')
setosa.imprime()
print setosa.calcula_entropia()
versicolor.imprime()
print versicolor.calcula_entropia()
virginica.imprime()
print virginica.calcula_entropia()

nos = []
nos.append(setosa)
nos.append(versicolor)
nos.append(virginica)
print "\n\n\n\n"
cria_no_raiz(nos)
