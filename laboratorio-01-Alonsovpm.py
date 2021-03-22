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
print((generador_cartas(numero_cartas)))
print(len((generador_cartas(numero_cartas))))
n=0
m=0

if len(generador_cartas(numero_cartas))%2==0:
    n=int(len(generador_cartas(numero_cartas))/2)
    m=2
if len(generador_cartas(numero_cartas))%3==0:
    n=int(len(generador_cartas(numero_cartas))/3)
    m=3
if len(generador_cartas(numero_cartas))%4==0:
    n=int(len(generador_cartas(numero_cartas))/4)
    m=4
if len(generador_cartas(numero_cartas))%5==0:
    n=int(len(generador_cartas(numero_cartas))/5)
    m=5
    
print(n) 

lista_tablero=[]
for i in range(m):
    lista_tablero.append([])
print(lista_tablero)

for i in range(m):
    for j in range(n):
        lista_tablero[i].append(generador_cartas(numero_cartas)[j])
print(lista_tablero)




