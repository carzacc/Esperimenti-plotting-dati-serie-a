#!/usr/bin/env python
'''
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
'''
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
import pandas as pd

df  = pd.read_csv("dati.csv")
print (df)
# Fixing random state for reproducibility

x = df['Tradizionale']
y = df['Gol Fatti']
plt.scatter(x, y)
plt.xlabel("Punti Tradizionale")
plt.ylabel("Gol Fatti")
plt.show()
