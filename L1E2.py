#Gustavo Alovisi
#Progressão Aritmética: enesimo termo e soma de termos

def progA(a1, r,n):
    an = a1 + (n-1)*r
    sn = (n/2)*(a1+an)
    lista = [an]
    lista.append(sn)
    return lista

valor = []
a1 = float(input("Informe o primeiro termo da PA:\n"))
r = float(input("Informe a razão da PA:\n"))
n = float(input("Informe o termo que deseja determinar:\n"))
valor = progA(a1,r,n)
print("O enesimo termo eh: ",valor[0])
print("A soma de termos ate n eh: ",valor[1])

