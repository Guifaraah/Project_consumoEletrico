import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [457, 447, 467, 506, 464, 503, 522, 523, 565, 519, 507, 507]

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y1 = [634, 620, 648, 702, 644, 698, 725, 726, 784, 720, 704, 704]


plt.bar(x1, y1, color='r', label = "Potência[KW]")
plt.plot(x, y, label = "Energia[KWh]", color='black', linestyle= 'solid', linewidth= 2.5)
plt.scatter(x, y, color='b')
plt.title("Gráfico consumo de energia elétrica (KWh) e Potência (KW)")
plt.legend()
plt.xlabel("Meses")
plt.ylabel("Consumo[KWh] x Potência[KW]")




plt.show()