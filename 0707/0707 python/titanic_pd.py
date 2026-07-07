import numpy as np
import pandas as pd

titanic = pd.read_csv(r"C:\Users\user\Desktop\파이썬-Express_학생용211105\파이썬 express 소스(2021.11)\sources\chap15\titanic.csv")

print(titanic["Age"].max())
