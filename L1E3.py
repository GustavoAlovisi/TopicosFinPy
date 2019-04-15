#Gustavo Alovisi
#Progressão Geométrica: enesimo termo e soma de termos

def progG(a1, q,n):
    an = a1 * (q ** (n-1))
    #sn = (n/2)*(a1+an)
    sn = 0
    for i in range(1,n+1):
        sn = sn + (a1*(q ** (i-1)))
    lista = [an]
    lista.append(sn)
    return lista

valor = []
a1 = float(input("Informe o primeiro termo da PG:\n"))
q = float(input("Informe a razão da PG:\n"))
n = int(input("Informe o termo que deseja determinar:\n"))
valor = progG(a1,q,n)
print("O enesimo termo eh: ",valor[0])
print("A soma de termos ate n eh: ",valor[1])