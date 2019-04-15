#Gustavo Alovisi
##Equação de Primeiro Grau - solver ax = b

import numpy as np


a = np.array([[4,5],[3,6]])
b = np.array([2,4])
x = np.linalg.solve(a,b)
print(x)