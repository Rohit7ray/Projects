import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')
from matplotlib.pyplot import figure

matplotlib.rcParams['figure.figsize'] = (12,8)


## LOADING DATA
df = pd.read_csv('movies.csv')
print(df)

## CLEANING DATA
#To check if we have null values or not
for col in df.columns:
  pct_missing = np.mean(df[col].isnull())
  print('{} - {}%'.format(col, pct_missing))

df.count()

## COUNTUNG NULL VLAUES
print((df.isnull().sum()))

## DROPPTING NULL VALUE
# df.columns
df = df.dropna(subset = ["released","score","votes","writer","star","country","runtime",'company'])

## HANDLING NULL VALUES

df["rating"] = df['rating'].fillna(df['rating'].mode()[0])
df['gross'] = df['gross'].fillna(df['gross'].mean())
df['budget'] = df['budget'].fillna(df['budget'].mean())

df.isnull().sum()

## DATATYPE CHECK
df.dtypes

## CHANGING DATA TYPE
df['budget'] = df['budget'].astype(int)
df['gross'] = df['gross'].astype(int)
df['votes'] = df['votes'].astype(int)
df['runtime'] = df['runtime'].astype(int)

print(df.head())
print(df['released'])
df['updated released date'] = df['released'].str.split('(').str[0].str.strip() #strip is used to remove unwanted elements

df['release year'] = df['updated released date'].astype('datetime64[ns]').dt.year

df['status'] = np.where(
    df["year"] != df["release year"],
    "Not matched",
    "matched"
)

print(df['status'])

df[df['status'] == 'Not matched'][['year', 'release year']]

df.sort_values(by = ["gross"], inplace = False, ascending = False)