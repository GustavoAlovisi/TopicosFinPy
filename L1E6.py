#Gustavo Alovisi
##Polinomio Solver

import numpy as np

grau = int(input("Insira o grau do polinomio: "))
lista = []

for i in range(0, grau):
    print("Insira o coeficiente a",i)
    if i==0:
        lista = [float(input())]
    else:
        lista.append(float(input()))

print(lista)

x = np.roots(lista)
print("As raizes do polinomio são: ", x)


valx = int(input("\nInforme o valor que vc deseja p x: "))

valp = np.polyval(lista, valx)

print("O valor do polinomio em x eh: ", valp)