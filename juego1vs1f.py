import random
from funcioneslistas import *


#recursos iniciales
hp_h = 100
pocion = 3
hp_e = 120
nombre_h=input("Inserte el nombre del heroe: ")
nombre_e=input("Inserte el nombre del enemigo: ")
accion_valida=True

lista=[nombre_h,hp_h,pocion,nombre_e,hp_e,accion_valida]
for i in range(0,len(lista)):
    print(lista[i])


opc = "0"
while hp_h>0 and hp_e >0:
    lista= turno_jugador(lista,opc)
    lista= turno_enemigo(lista)
    hp_e=int(lista[4])
    hp_h=int(lista[1])
    accion_valida=True
    lista[5]=accion_valida
    opc = "0" 
    