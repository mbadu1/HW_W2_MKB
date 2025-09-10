import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read csv file downloaded from kaggle
df = pd.read_csv('gold_data_2015_25.csv')
print(df.head())
print(df.info())
print(df.describe())
#Change date to actual datetime type
df['Date'] = pd.to_datetime(df['Date'])
print(df.info())
print(df.loc[df['Date'].dt.year == 2025])
print(df.groupby(df['Date'].dt.year)[['SPX','GLD']].mean())
print(df.groupby(df['Date'].dt.year)[['SPX','GLD']].count())
df = df.set_index('Date')
print(df.head())
# Compute and print correlation matrix between variables
print(df.corr())
print(sns.heatmap(df.corr(), cmap="coolwarm"))
print(df['SPX'].plot())
from sklearn.linear_model import LinearRegression
#Looking into the regression of the data
lr=LinearRegression()
# Define target variable (y) and features (x)
y = df['SPX']
x = df[['GLD', 'SLV']]
# Train the regression model
lr.fit(x,y)
# Predict SPX values using trained model
predict = lr.predict(x)
sns.lineplot(data=df,y='SPX',x=df.index)
# Plot predicted SPX values over time
sns.lineplot(y=predict,x=df.index)
from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error
# Evaluate model performance with error metrics
print(mean_absolute_error(y,predict))
print(mean_absolute_percentage_error(y,predict))
