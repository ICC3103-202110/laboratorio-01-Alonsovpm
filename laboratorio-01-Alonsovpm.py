import random

def generador_cartas(numero_cartas):
    lista_cartas: []
    for i in range(numero_cartas):
        n = random.randint(1,numero_cartas)
        lista_cartas.append(n)

numero_cartas: input("Con cuantas cartas desea jugar: ")
