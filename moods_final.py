import pandas as pd
import numpy as numpy

df = pd.read_csv('artists_chartic.csv', encoding='utf-8')

print(df.head())
print(df.describe())