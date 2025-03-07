# Creación de una matriz 3D de ejemplo: ciudades, días de la semana, semanas
# 3 ciudades, 7 días, 2 semanas
temperaturas = [
    [  # Ciudad 1
        [30, 32, 33, 34, 35, 31, 30],  # Semana 1
        [29, 28, 31, 32, 30, 29, 27],  # Semana 2
    ],
    [  # Ciudad 2
        [25, 26, 24, 27, 28, 29, 25],  # Semana 1
        [26, 27, 25, 28, 26, 24, 23],  # Semana 2
    ],
    [  # Ciudad 3
        [20, 21, 22, 23, 24, 22, 21],  # Semana 1
        [22, 23, 21, 20, 22, 23, 24],  # Semana 2
    ]
]

# Calcular el promedio por ciudad para cada semana
for ciudad_index, ciudad in enumerate(temperaturas):
    print(f"Promedios para la Ciudad {ciudad_index + 1}:")
    for semana_index, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)
        print(f"  Semana {semana_index + 1}: {promedio:.2f}°C")
