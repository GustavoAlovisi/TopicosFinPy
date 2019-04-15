#Gustavo Alovisi
##Solver de equação de segundo grau

import math

a = int(input("Insira o termo 'a' da eq.: "))
b = int(input("Insira o termo 'b' da eq.: "))
c = int(input("Insira o termo 'c' da eq.: "))


def solver(a,b,c):
    x1 = (-b + math.sqrt((b*b)-(4*a*c)))/(2*a)
    x2 = (-b - math.sqrt((b*b)-(4*a*c)))/(2*a)
    return [x1,x2]

x = solver(a,b,c)

print("X1 = ", x[0])
print("X2 = ", x[1])