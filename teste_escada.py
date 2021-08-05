import numpy as np
import matplotlib.pyplot as plt


# tiros_cz_550 = [2656, 2667, 2657,
#                  2667, 2681, 2730,
#                  2749, 2726, 2755,
#                  2794, 2805]

tiros = [2557, 2538, 2579,
         2559, 2603, 2600,
         2611, 2618, 2641,
         2634, 2649]

polvora = [i for i in np.arange(39.5, 41.6, 0.2)]
print(polvora)

fig, ax = plt.subplots(figsize=(16,9))
fig.figsize = (16, 9)
plt.xticks(np.arange(39.5, 41.5, 0.2))
ax.plot(polvora, tiros, 'bo-')

for x,y in zip(polvora,tiros):

    label = "{:.2f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.title("Teste de Escada")
plt.xlabel("Peso polvora 102 (gn)")
plt.ylabel("Velocidade pés/s")
plt.savefig("Teste_escada.png")
plt.show()
