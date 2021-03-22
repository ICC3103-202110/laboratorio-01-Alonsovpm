import random

def generador_cartas(numero_cartas):
    lista_cartas = []
    for i in range(numero_cartas):
        n = random.randint(1,numero_cartas)
        lista_cartas.append(n)
    for i in range(len(lista_cartas)):
        lista_cartas.append(lista_cartas[i])
    return lista_cartas

numero_cartas = int(input("Con cuantas cartas desea jugar: "))
print(generador_cartas(numero_cartas))