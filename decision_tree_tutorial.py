#!/usr/bin/env python
#encoding:utf8

import sys
from metodos_utilitarios import *
import os

if __name__ == "__main__":
    os.system('clear')
    baseDeDados = carrega_csv(sys.argv[1])
    arvore=montaArvore(baseDeDados)
    mostraArvore(arvore)
