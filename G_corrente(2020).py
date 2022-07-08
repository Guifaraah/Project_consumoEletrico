import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [6.05, 5.65, 6.08, 5.56, 5.69, 5.63, 5.90, 5.86, 5.68, 5.93, 5.85, 5.96]

ax = plt.axes()


plt.plot(x, y, color='b')
plt.scatter(x, y, color='black')
plt.title("Gráfico de Corrente elétrica (KA)")
plt.xlabel("Meses")
plt.ylabel("Corrente elétrica[KA]")




plt.show()