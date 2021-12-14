import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados = pd.read_csv(r'C:\Users\Lucas\Desktop\grafico.csv', delimiter=';', skiprows=0, low_memory=False)
df=pd.DataFrame(dados, columns=["meta para a inflação","IPCA ocorrido","limite mínimo","limite máximo","Focus mais recente"])

df.plot(xlabel="Tempo (a cada 20 meses)", ylabel="Var. %")
plt.show() 


