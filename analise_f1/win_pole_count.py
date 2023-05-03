import pandas as pd
import numpy as np

#Conta a quantidade de vitórias e pole position por piloto

#Abertura dos arquivos de dados CSV
f1_results = pd.read_csv("analise_f1\\f1_data\\results.csv")
drivers = pd.read_csv("analise_f1\\f1_data\drivers.csv")
drivers_reduced = drivers.drop(columns=['dob', 'url']) #Retira dados relevantes do DF de pilotos

#Converter os dados de Posição e Grid para númerico 
f1_results['position'] = pd.to_numeric(f1_results['position'], errors='coerce')
f1_results['grid'] = pd.to_numeric(f1_results['grid'], errors='coerce')

#Filtragem dos dados de vitória (position == 1) e pole positio (grid == 1)
winner_results = f1_results[(f1_results.position == 1)]
pole_results = f1_results[(f1_results.grid == 1)]

#Reduz os DFs de vencedores e pole position - apenas colunas relevantes
winner_results_reduced = winner_results[['resultId', 'driverId', 'grid', 'position', 'points']]
pole_results = pole_results[['resultId', 'driverId', 'grid', 'position', 'points']]

#Cria DFs para armazenar os dados do ID e número de vitórias/pole
winner_count = winner_results[['driverId', 'position']]
pole_count = pole_results[['driverId', 'grid']]

#Renomeia as colunas para contar o número de vitórias e poles
winner_count = winner_count.rename(columns={'driverId': 'driverId', 'position': 'winCount'}) 
pole_count = pole_count.rename(columns={'driverId': 'driverId', 'grid': 'poleCount'}) 

#Agrupa os dados pelo ID do piloto e soma a quantidade de vitórias/poles
winner_count = winner_count.groupby('driverId').sum()
pole_count = pole_count.groupby('driverId').sum()

#Cria um DF a partir de uma join com os DFs de contagem de vitórias/poles
drivers_wincount = pd.merge(drivers_reduced, winner_count, how='left', on='driverId')

drivers_wincount = drivers_wincount.sort_values(by = ['winCount'], ascending=False) #Ordena o DF criado com base no número de vitórias

drivers_wincount = pd.merge(drivers_wincount, pole_count, how='left', on='driverId')

print(drivers_wincount.head(10))

#Próximo passo: verificar a taxa de conversão de poles em vitórias - porcentagem de vezes que iniciou na pole e venceu.






