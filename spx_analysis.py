import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gold_data_2015_25.csv')
print(df.head())
print(df.info())
print(df.describe())
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())