import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [4.99, 4.88, 5.10, 5.52, 5.07, 5.49, 5.70, 5.71, 6.17, 5.66, 5.54, 5.54]

ax = plt.axes()


plt.plot(x, y, color='b')
plt.scatter(x, y, color='black')
plt.title("Gráfico de Corrente elétrica (KA)")
plt.xlabel("Meses")
plt.ylabel("Corrente elétrica[KA]")




plt.show()