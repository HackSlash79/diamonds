import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





url = 'https://raw.githubusercontent.com/HackSlash79/diamonds/main/diamonds.csv'
df = pd.read_csv(url, index_col=0)

firstSeven = df.head(7)
lastSeven = df.tail(7)
print(firstSeven)
print(lastSeven)

desc = df.describe()
desc

cutDescribe = df.cut.describe()
cutDescribe

colorDescribe = df.color.describe()
colorDescribe

clarityDescribe = df.clarity.describe()
clarityDescribe

hist = df.hist()
hist
