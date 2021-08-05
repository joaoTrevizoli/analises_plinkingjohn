import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 2570, 20 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, density=True)



plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')


plt.xlim(2500, 2640)

plt.title("Função densidade(\"Probabilidade\")")
plt.xlabel("Velocidade na saida do cano")
plt.ylabel("Fx (x) densidades")

plt.show()