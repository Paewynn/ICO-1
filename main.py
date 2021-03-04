# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:18:36 2021

@author: Julien
"""

from evolution_functions import next_gen, init_pop
from constants import nb_generations, nb_pop

import matplotlib.pyplot as plt

###############################################################################
#######################   génération de la population  ########################
###############################################################################
population=init_pop(nb_pop)

X=[1]
Y=[population[0][1]]

for i in range(2,nb_generations+1):
    population = next_gen(population)
    X.append(i)
    Y.append(population[0][1])
plt.plot(X,Y)
    
#    if i%100 == 0: 
#        print(population[0][1])
    
plt.savefig(str(population[0][1])+'_distance.png', format='png')    

"""

# #on genere une carte représentant notre solution
#lons = []
#lats = []
#noms = []
#for i in population[0][0]:
#    lons.append(Villes[i][1])
#    lats.append(Villes[i][0])
#    noms.append(Villes[i][2])
#
#y = lons
#z = lats
#n = noms
#
#fig, ax = plt.subplots()
#ax.scatter(z, y)
#ax.plot(z,y)
#
#for i, txt in enumerate(n):
#    ax.annotate(txt, (z[i], y[i]))
#
#
#plt.savefig(str(population[0][1])+'chemin.png', format='png') 

"""
