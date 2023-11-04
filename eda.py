import pandas as pd
import os
import sys
import subprocess


if len(sys.argv) != 2:
    print("Usage: vis.py <data_frame_path>")
    sys.exit(1)

data_frame_path = sys.argv[1]


df = pd.read_csv(data_frame_path)

df.groupby(['Education','Marital_Status'])['ID'].count().unstack()


with open('eda-in-1.txt', 'a') as f:
    f.write(f"Insight 1: You can have a PhD and still be unmature.\n")



with open('eda-in-1.txt', 'a') as f:
    f.write(f"Insight 2: Income has high variance. std = {df.describe().loc['std','Income']}.\n")


for col in df.corr():
    for row in df.corr()[col]:
        if row == 1:
            continue
        if row > 0.7:
            print(col)


df.corr().loc['MntMeatProducts','NumCatalogPurchases']

with open('eda-in-1.txt', 'a') as f:
    f.write(f"Insight 3: MntMeatProducts and NumCatalogPurchases are highly correlated, corr = {df.corr().loc['MntMeatProducts','NumCatalogPurchases']}.\n")

subprocess.call(["python", "vis.py", data_frame_path])

# os.system(f"python vis.py {data_frame_path}")