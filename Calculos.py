def maximo_goleador(datos):
    maximo_goles=-1
    max_goleador=""
    for jugador in datos.keys():
        if (datos[jugador]["Goles_favor"] > maximo_goles):
            maximo_goles=datos[jugador]["Goles_favor"]
            
    print(datos[jugador]["Goles_favor"])
