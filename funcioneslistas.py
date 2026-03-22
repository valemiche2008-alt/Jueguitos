def salud(n:int):
    mostrar_ico = ""
    corazones="❤️"
    n=n//10
    for i in range(0,n,1):
        mostrar_ico = mostrar_ico + corazones
    return mostrar_ico

def turno_jugador(lista,opc):
    import random
    while opc != "1" and opc != "2" and opc != "3":
    
        opc = input("Por favor escoge una opcion:""\n 1.Atacar" \
        "\n 2.Curar" \
        "\n 3.Habilidad especial" \
        "\n Dijite el numero eleccion:")
        if  opc != "1" and opc != "2" and opc != "3":
            print("Opcion invalida, porfa intente de nuevo")
            

    #acciones dependiendo de la accion
    nombre_h=lista[0]
    hp_e=int(lista[4])
    hp_h=int(lista[1])
    pocion=int(lista[2])
    accion_valida=bool(lista[5])
    if opc == "1":
        print(f"==TURNO DEL HEROE {nombre_h}==")
        daño_aleatorio = random.randint(10,25)
        print("El daño del heroe fue ",daño_aleatorio)
        hp_e = hp_e - daño_aleatorio 
        if hp_e <=0:
            print("Haz derrotado al enemigo")
            hp_e =0
        print("Vida del enemigo ", hp_e)
        print(salud(hp_e))
        lista[4]=hp_e


    elif opc == "2":
        print(f"==TURNO DEL HEROE {nombre_h}==")
        if pocion >= 1:
            hp_h = hp_h + 20
            print("Vida actual del heroe:",hp_h)
            print(salud(hp_h))
            pocion = pocion -1
            print("Pociones restantes", pocion)
        else:
            print("No te quedan mas pociones, intenta de nuevo")
            opc = "0"
            accion_valida=False
        lista[5]=accion_valida    
        lista[1]=hp_h
        lista[2]=pocion

    elif opc == "3":
        print(f"==TURNO DEL HEROE {nombre_h}==")
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
        print(salud(hp_e))
        lista[4]=hp_e
    return lista

def turno_enemigo(lista):
    import random
    #ataque del enemigo
    nombre_e=lista[3]
    accion_valida=bool(lista[5])
    hp_e=int(lista[4])
    hp_h=int(lista[1])
    if accion_valida==True:
        if hp_e > 0:
            print(f"==TURNO DEL ENEMIGO {nombre_e}==")
            daño_aleatorio_ene = random.randint(15,20)
            print("El Daño del enemigo fue",daño_aleatorio_ene)
            hp_h = hp_h - daño_aleatorio_ene
            lista[1]=hp_h
        if hp_h <=0:
            print("El enemigo te ha derrotado")
            hp_h = 0
            lista[1]=hp_h
        print("La vida del heroe es:",hp_h)
        print(salud(hp_h))
    return lista
        