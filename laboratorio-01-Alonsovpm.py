import random

def generador_cartas(numero_cartas):
    lista_cartas = []
    for i in range(numero_cartas):
        lista_cartas.append(i+1)
    for i in range(len(lista_cartas)):
        lista_cartas.append(lista_cartas[i])
    random.shuffle(lista_cartas)
    return lista_cartas

def imprimir_tablero(lista1,lista2,ptj1,ptje2):
    print("PUNTAJE J1: "+str(ptje1)+" PUNTAJE J2: "+str(ptje2))
    for i in range(len(lista1)):
        for j in range(len(lista1[i])):
            print(" _____ ", end="")
        print("")
        for j in lista1[i]:
            print("|     |", end="")
        print("")
        for j in range(len(lista1[i])):
            print("|  "+str(lista2[i][j])+"  |", end="")
        print("")
        for j in lista1[i]:
            print("|_____|", end="")
        print("")
        for j in range(len(lista1[i])):
            print(lista1[i][j], end=" ")
        print("")

def dar_vuelta(lista_censurada_tablero,lista_tablero,contador):   
    turno=0
    if contador%2==0:
        turno = 2
    elif contador%2!=0:
        turno = 1

    darvuelta = input("Jugador "+str(turno)+" Escriba las coordenadas de la carta que desea dar vuelta(ej:0,1): ")
    coord = darvuelta.split(",")
    for i in range(len(coord)):
        coord[i]= int(coord[i])
    lista_censurada_tablero[coord[0]][coord[1]] = lista_tablero[coord[0]][coord[1]]
    imprimir_tablero(lista_coord_tablero,lista_censurada_tablero,ptje1,ptje2)

    darvuelta = input("Jugador "+str(turno)+" Escriba las coordenadas de la carta que desea dar vuelta(ej:0,1): ")
    coord2 = darvuelta.split(",")

    for i in range(len(coord2)):
        coord2[i]= int(coord2[i])
    lista_censurada_tablero[coord2[0]][coord2[1]] = lista_tablero[coord2[0]][coord2[1]]
    imprimir_tablero(lista_coord_tablero,lista_censurada_tablero,ptje1,ptje2)
    
    
    if lista_tablero[coord2[0]][coord2[1]] == lista_tablero[coord[0]][coord[1]] and coord != coord2:
        print("son iguales!")
        lista_censurada_tablero[coord[0]][coord[1]] = " "
        lista_censurada_tablero[coord2[0]][coord2[1]] = " "
        return lista_censurada_tablero, turno

    elif coord == coord2:
        print("Introduza coordenadas distintas, intentelo denuevo")
        lista_censurada_tablero[coord[0]][coord[1]] = "?"
        lista_censurada_tablero[coord2[0]][coord2[1]] = "?"
        return lista_censurada_tablero, 0

    else:
        print("no son iguales intentalo denuevo")
        lista_censurada_tablero[coord[0]][coord[1]] = "?"
        lista_censurada_tablero[coord2[0]][coord2[1]] = "?"
        return lista_censurada_tablero, 0
        
numero_cartas = int(input("Con cuantas cartas desea jugar: "))

lista_cartas = generador_cartas(numero_cartas)

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

lista_tablero=[]
for i in range(n):
    lista_tablero.append([])

k=0
for i in range(n):
    for j in range(m):
        lista_tablero[i].append(lista_cartas[j+k])
    k+=m

#tablero coord
lista_coord=[]
for x in range(n):
    for y in range(m):
        lista_coord.append((x,y))

lista_coord_tablero=[]
for i in range(n):
    lista_coord_tablero.append([])
k=0
for i in range(n):
    for j in range(m):
        lista_coord_tablero[i].append(lista_coord[j+k])
    k+=m

lista_censurada=[]
for x in range(n):
    for y in range(m):
        lista_censurada.append((x,y))

lista_censurada_tablero=[]
for i in range(n):
    lista_censurada_tablero.append([])
k=0
for i in range(n):
    for j in range(m):
        lista_censurada_tablero[i].append("?")
    k+=m

lista_final=[]
for i in range(n):
    lista_final.append([])
k=0
for i in range(n):
    for j in range(m):
        lista_final[i].append(" ")
    k+=m

ptje1=0
ptje2=0
contador=1

imprimir_tablero(lista_coord_tablero,lista_censurada_tablero,ptje1,ptje2)
funciondarvuelta = dar_vuelta(lista_censurada_tablero,lista_tablero,contador)

lista_actualizada = funciondarvuelta[0]
puntaje = funciondarvuelta[1]
if puntaje == 1:
    ptje1+=1
if puntaje == 2:
    ptje2+=1
imprimir_tablero(lista_coord_tablero,lista_censurada_tablero,ptje1,ptje2)

while lista_actualizada != lista_final:
    contador+=1
    funciondarvuelta = dar_vuelta(lista_censurada_tablero,lista_tablero,contador)

    lista_actualizada = funciondarvuelta[0]
    puntaje = funciondarvuelta[1]
    if puntaje == 1:
        ptje1+=1
    if puntaje == 2:
        ptje2+=1
    imprimir_tablero(lista_coord_tablero,lista_censurada_tablero,ptje1,ptje2)

print("El juego termino!")






