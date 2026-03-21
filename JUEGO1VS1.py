import random


#recursos iniciales

hp_h = 100
pocion = 3
hp_e = 120
opc = "0"
while hp_h>0 and hp_e >0:
    while opc != "1" and opc != "2" and opc != "3":
    
        opc = input("Por favor escoge una opcion:""\n 1.Atacar" \
        "\n 2.Curar" \
        "\n 3.Habilidad especial" \
        "\n Dijite el numero eleccion:")
        if  opc != "1" and opc != "2" and opc != "3":
            print("Opcion invalida, porfa intente de nuevo")
            

    #acciones dependiendo de la accion

    if opc == "1":
        print("==TURNO DEL HEROE==")
        daño_aleatorio = random.randint(10,25)
        print("El daño del heroe fue ",daño_aleatorio)
        hp_e = hp_e - daño_aleatorio 
        if hp_e <=0:
            print("Haz derrotado al enemigo")
            hp_e =0
        print("Vida del enemigo ", hp_e)


    elif opc == "2":
        print("==TURNO DEL HEROE==")
        if pocion >= 1:
            hp_h = hp_h + 20
            print("Vida actual del heroe:",hp_h)
            pocion = pocion -1
            print("Pociones restantes", pocion)
        else:
            print("No te quedan mas pociones, intenta de nuevo")
            opc = "0"
            continue

    elif opc == "3":
        print("==TURNO DEL HEROE==")
        habilidad_especial = random.randint(30,50)
        print("Ataque critico de: ",habilidad_especial)
        aleatorio = random.randint(1,100)
        if aleatorio >= 1 and aleatorio <= 50:
            print("Ataque critico acertado, el heroe causa daño de: ",habilidad_especial)
            hp_e = hp_e - habilidad_especial
        else:
            print("Ataque del heroe fallido")
        if hp_e <=0:
            print("Haz derrotado al enemigo")
            hp_e =0
        print("vida de enemigo",hp_e)
        

    #ataque del enemigo 
    if hp_e > 0:
        print("==TURNO DEL ENEMIGO==")
        daño_aleatorio_ene = random.randint(15,20)
        print("El Daño del enemigo fue",daño_aleatorio_ene)
        hp_h = hp_h - daño_aleatorio_ene
        
        if hp_h <=0:
            print("El enemigo te ha derrotado")
            hp_h = 0
        print("La vida del heroe es:",hp_h)
    opc = "0" 
    