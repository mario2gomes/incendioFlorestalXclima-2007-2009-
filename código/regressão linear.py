# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:31:41 2017

@author: mário
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

caminho = '../tabelas/'
atributos = (('DADOS2009 - vento.xlsx','vento'),('DADOS2009 - temperatura.xlsx','temperatura'),
             ('DADOS2009 - humidade.xlsx','humidade'),('DADOS2009 - chuva.xlsx','chuva'))

for (a,b) in atributos:
    train_dataset = pd.read_excel(caminho+a)

    X = train_dataset[b]
    Y = train_dataset['incendios']

#slope = inclinacao
    slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)
    erroquadratico = r_value ** 2

    print("\n\nCorrelação "+b+" x Incêndios\n")
    print("Erro quadratico: {:.4f}".format(erroquadratico))
    
    print("(Beta)_Inclinacao:{:.4f}".format(slope))
    print("(Alpha)_intercept: {:.4f}".format(intercept))
    print("Coeficiente__Correlacao:{:.4f}".format(r_value))
    
    print ("P_Value:", p_value)
    print("Erro_do_Desvio_Padrao: {:.4f}".format(std_err))
    
'''    print("qual o valor para "+b+" ?")
    X = float(input())
    Y = intercept + slope*X
    print("quantidade de incêndios previstos: {:.4f}".format(Y))
    '''