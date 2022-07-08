import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [554, 517, 556, 509, 521, 515, 540, 536, 520, 543, 535, 545]

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y1 = [769, 718, 772, 706, 723, 715, 750, 744, 722, 754, 743, 756]


plt.bar(x1, y1, color='r', label = "Potência[KW]")
plt.plot(x, y, label = "Energia[KWh]", color='black', linestyle= 'solid', linewidth= 2.5)
plt.scatter(x, y, color='b')
plt.title("Gráfico consumo de energia elétrica (KWh) e Potência (KW)")
plt.legend()
plt.xlabel("Meses")
plt.ylabel("Consumo[KWh] x Potência[KW]")




plt.show()