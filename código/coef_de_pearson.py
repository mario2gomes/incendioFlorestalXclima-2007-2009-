import pandas as pd
import numpy as np
#the csv file is located in a previous subdirectory called tables

caminho = "../tabelas/"
atributos = (('DADOS2009 - vento.xlsx','vento'),('DADOS2009 - temperatura.xlsx','temperatura'),
             ('DADOS2009 - humidade.xlsx','humidade'),('DADOS2009 - chuva.xlsx','chuva'))

for (a,b) in atributos:
    
    print("\n"+b+"\n")
    train_dataset = pd.read_excel(caminho+a)
    X = train_dataset[b]
    Y = train_dataset['incendios']
    mediaX = np.mean(X)
    mediaY = np.mean(Y)
    stdX = np.std(train_dataset[b], ddof=1)
    stdY = np.std(train_dataset['incendios'], ddof=1)
#Means Delta Degrees of Freedom. The divisor used in calculations is
    #N - ddof, where N represents the number of elements. By default ddof is zero.
#Because this parameter we get the diference between
    print("Media_X:{:5.2f}".format(mediaX))
    print("Media_Y: {:5.2f}".format(mediaY))
    print("Desvio_Padrao_X: {:5.2f}".format(stdX))
    print("Desvio_Padrao_Y: {:5.2f}".format(stdY))
    deviationX = X - mediaX
    deviationY = Y - mediaY
    sumCovariance = np.sum(deviationX*deviationY)
    print("Soma_da_covariancia: {:5.2f}".format(sumCovariance))
#Number of instances
    N = train_dataset.shape[0]
    print("Instâncias: ",N)
    pearsonCorrelation = sumCovariance/((N-1)*stdX*stdY)
    print("Correlacao (coeficiente de pearson): {:4f}".format(pearsonCorrelation))
        
    beta = pearsonCorrelation * (stdY/stdX)
    alpha = mediaY-(beta*mediaX)
    print("Beta: {:5.2f}".format(beta))
    print ("Alpha: {:5.2f}".format(alpha))