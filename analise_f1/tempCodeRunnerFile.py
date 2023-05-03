import pandas as pd
import numpy as np

f1_results = pd.read_csv("analise_f1\\f1_data\seasons.csv")
drivers = pd.read_csv("analise_f1\\f1_data\drivers.csv")

f1_winner_results = f1_results[(f1_results.position == 1)]

print(f1_winner_results.head())

