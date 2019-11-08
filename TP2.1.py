import numpy as np
import pandas as pd

# x = pd.read_csv ("data.csv")
data = pd.read_csv('data.csv', header=0)
print(data)
# print(data._series[A])

A = pd.tseries