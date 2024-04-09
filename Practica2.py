names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA,
CESAR, David, Diego, Dolores, DYLAN, ELIANA, Emanuel, Fabián, Noelia,
Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0,
11]
goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2,
3, 0, 0]
assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1,
0]

names = [name.strip() for name in names.split(",")]
print(names)
diccionario_datos={}
for i in range(len(names)):
    diccionario_datos[names[i]] = {
        "Goles_favor" : goals[i],
        "Goles_evitados" : goals_avoided[i],
        "Asistencias" : assists[i]
    }
print(2)


