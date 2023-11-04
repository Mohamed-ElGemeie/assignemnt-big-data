# Data Preprocessing
import pandas as pd
import sys
import os
import subprocess

if len(sys.argv) != 2:
    print("Usage: vis.py <data_frame_path>")
    sys.exit(1)

data_frame_path = sys.argv[1]

df = pd.read_csv(data_frame_path)
df.head(10)
print(df.shape)
print(df.columns)
### Data Cleaning
df.isnull().mean()
# Dop null values
print(df['Income'].mean())
df['Income'] = df['Income'].fillna(df['Income'].mean())
print(df['Income'].isnull().sum())
print(df['Income'].mean())
print(df['Marital_Status'].value_counts())
print(df['Education'].value_counts())
# Drop unnecessary categories
for i in range(df.shape[0]):
    if (df['Marital_Status'][i] == 'Absurd') or (df['Marital_Status'][i] == 'Alone') or (df['Marital_Status'][i] == 'YOLO'):
        df.drop(index=i, inplace=True)
print(df.shape)
print(df['Marital_Status'].value_counts())
### Data Transformation
import matplotlib.pyplot as plt
import numpy as np
plt.hist(df['Income'],range=[0,300000],edgecolor='black')
df['Income'] = df['Income'].transform(np.log10)
plt.hist(df['Income'],edgecolor='black')
df['dt_day_customer'] = df['Dt_Customer'].apply(lambda row: row.split('-')[0])
df['dt_month_customer'] = df['Dt_Customer'].apply(lambda row: row.split('-')[1])
df['dt_year_customer'] = df['Dt_Customer'].apply(lambda row: row.split('-')[2])
df.drop(columns=['Dt_Customer'], inplace=True)
df.head()
from datetime import date
df['age'] = date.today().year - df['Year_Birth']
df.drop(columns='Year_Birth',inplace=True)
df.head()
### Data Discretization
df['class'] = pd.cut(df['Income'], 3, labels=['poor','middle','rich'])
df['class'].value_counts()
onehotencoding = pd.get_dummies(df[['Education','Marital_Status','class']], dtype=int)
onehotencoding.head()
df.drop(columns=['Education','Marital_Status','class'], inplace=True)
df = pd.concat([df,onehotencoding], axis=1)
df.head()
### Data Reduction
df.describe()
# Drop Low Variance Columns
df['Income'].std()
num_df = df.drop(columns=['ID','dt_day_customer','dt_month_customer','dt_year_customer'])
for col in num_df.columns:
    if df[col].std() < 0.2:
        df.drop(columns=col, inplace=True)
print(df.shape)
print(df.columns)
# Drop Unneccesary Columns
df.drop(columns='ID', inplace=True)
df.corr().head()
# Drop Highly Correlated Features
size = df.corr().shape[0]
for i in range(size):
    for j in range(size):
        if df.corr().iloc[i,j] == 1:
            continue
        if df.corr().iloc[i,j] >= 0.6:
            try:
                df.drop(j, axis=1)
            except:
                continue
print(df.shape)
print(df.columns)
# Save File
df.to_csv('res_dpre.csv')

subprocess.call(["python", "eda.py", os.getcwd()+"\\res_dpre.csv"])

# os.system(f"python eda.py {os.getcwd()+"\\res_dpre.csv"}")