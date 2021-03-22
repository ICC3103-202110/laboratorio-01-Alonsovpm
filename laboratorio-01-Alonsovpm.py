import random

def generador_cartas(numero_cartas):
    lista_cartas = []
    for i in range(numero_cartas):
        n = random.randint(1,numero_cartas)
        lista_cartas.append(n)
    for i in range(len(lista_cartas)):
        lista_cartas.append(lista_cartas[i])
    random.shuffle(lista_cartas)
    return lista_cartas

numero_cartas = int(input("Con cuantas cartas desea jugar: "))

lista_cartas = generador_cartas(numero_cartas)

print(lista_cartas)
print(len((lista_cartas)))
n=0
m=0

if len(lista_cartas)%2==0:
    n=int(len(lista_cartas)/2)
    m=2
if len(lista_cartas)%3==0:
    n=int(len(lista_cartas)/3)
    m=3
if len(lista_cartas)%4==0:
    n=int(len(lista_cartas)/4)
    m=4
if len(lista_cartas)%5==0:
    n=int(len(lista_cartas)/5)
    m=5

print(n) 
lista_tablero=[]
for i in range(n):
    lista_tablero.append([])
print(lista_tablero)
k=0
for i in range(n):
    for j in range(m):
        lista_tablero[i].append(lista_cartas[j+k])
    k+=m
print(lista_tablero)

for i in range(len(lista_tablero)):
    for j in lista_tablero[i]:
        print(j, end="")
    print("")



