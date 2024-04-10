def maximo_goleador(datos):
    maximo_goles=-1
    max_goleador=""
    for jugador in datos.keys():
        if (datos[jugador]["Goles_favor"] > maximo_goles):
            maximo_goles=datos[jugador]["Goles_favor"]
            max_goleador=jugador
    return (max_goleador,maximo_goles)

def jugador_mas_influyente(datos):
    mas_influyente=""
    puntos_max=-1
    for jugador in datos.keys():
        puntos=datos[jugador]["Goles_favor"] * 1.5 + datos[jugador]["Goles_evitados"] * 1.25 + datos[jugador]["Asistencias"] * 1
        if (puntos > puntos_max):
            mas_influyente=jugador
            puntos_max=puntos
    print ("El jugador mas influyente es", mas_influyente, "con", puntos_max, "puntos.")

def promedio_goles(datos):
    goles = 0
    for jugador in datos.keys():
        goles=goles + datos[jugador]["Goles_favor"] 
    
    print ("El promedio de goles es", goles/25, "goles por partido.")

def promedio_goles_mas_influyente(datos):
    goleador,goles=maximo_goleador(datos)
    goles_goleador = datos[goleador]["Goles_favor"]
    print ("El promedio de goles del goleador", goleador, "es", goles_goleador/25, "goles.")

    

