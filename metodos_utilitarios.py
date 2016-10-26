import csv
from math import log
from noArvore import *

def carrega_csv(arquivo_csv):
    arrayDestino = []
    with open(arquivo_csv, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0: continue
            arrayDestino.append(r)
    f.close()
    return arrayDestino

def divideTabela(rows,column,valor):

   divide_tabela=None
   if isinstance(valor,int) or isinstance(valor,float):
      divide_tabela=lambda row:row[column]>=valor
   else:
      divide_tabela=lambda row:row[column]==valor

   conjunto1=[row for row in rows if divide_tabela(row)]
   conjunto2=[row for row in rows if not divide_tabela(row)]
   return (conjunto1,conjunto2)

def contabilizaUltimaColuna(rows):
   resultados={}
   for row in rows:
      r=row[len(row)-1]
      if r not in resultados: resultados[r]=0
      resultados[r]+=1
   return resultados

def entropia(rows):

   log2=lambda x:log(x)/log(2)
   resultados=contabilizaUltimaColuna(rows)

   ent=0.0
   for r in resultados.keys():
      p=float(resultados[r])/len(rows)
      ent=ent-p*log2(p)
   return ent

def contabilizaUltimaColuna(rows):
   resultados={}
   for row in rows:
      r=row[len(row)-1]
      if r not in resultados: resultados[r]=0
      resultados[r]+=1
   return resultados

def montaArvore(rows,pontuacao=entropia):

  if len(rows)==0: return noArvore()
  pontuacao_corrente=pontuacao(rows)

  melhor_ganho=0.0
  melhor_criterio=None
  melhor_conjunto=None

  total_coluna=len(rows[0])-1

  for col in range(0,total_coluna):

    global valores_das_colunas
    valores_das_colunas={}
    for row in rows:
       valores_das_colunas[row[col]]=1

    for valor in valores_das_colunas.keys():
      (conjunto1,conjunto2)=divideTabela(rows,col,valor)

      p=float(len(conjunto1))/len(rows)
      ganho=pontuacao_corrente-p*pontuacao(conjunto1)-(1-p)*pontuacao(conjunto2)
      if ganho>melhor_ganho and len(conjunto1)>0 and len(conjunto2)>0:
        melhor_ganho=ganho
        melhor_criterio=(col,valor)
        melhor_conjunto=(conjunto1,conjunto2)
  if melhor_ganho>0:
    trueBranch=montaArvore(melhor_conjunto[0])
    falseBranch=montaArvore(melhor_conjunto[1])
    return noArvore(col=melhor_criterio[0],valor=melhor_criterio[1],
                        tb=trueBranch,fb=falseBranch)
  else:
    return noArvore(resultados=contabilizaUltimaColuna(rows))

def mostraArvore(arvore,indent=''):
    if arvore.resultados==None:
        print "[",arvore.valor,"]"
        print indent,
        mostraArvore(arvore.tb,indent+'  ')
        print indent,
        mostraArvore(arvore.fb,indent+'  ')
        
