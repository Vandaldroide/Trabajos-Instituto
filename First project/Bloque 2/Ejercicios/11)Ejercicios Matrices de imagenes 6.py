import AMS_compression as amsc

ruta_imagen = input("Ruta o nombre de la imagen a comprimir:\n")
ruta_imagen_comprimida = input("Ruta o nombre de la imagen comprimida:\n")

# Leer imagen
matriz_r, matriz_g, matriz_b, ancho, alto = amsc.imagen_a_matrices(ruta_imagen)


######################################################################
##### ESCRIBE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES A CONTINUACIÓN #####
######################################################################

# Las matrices de la imagen original son matriz_r, matriz_g y matriz_b
# una para cada canal.
# Crea tres matrices nuevas llamadas: comprimida_r, comprimida_g y
# comprimida_b con el fin de comprimir las matrices de la imagen 
# original.
# Utiliza los diferentes métodos de compresión explicados por el 
# profesor en clase.
#desescalar imagen
comprimida_r = []
comprimida_g = []
comprimida_b = []
for i in range(0,alto,2):
    comprimida_r.append([])
    comprimida_g.append([])
    comprimida_b.append([])
    for j in range(0,ancho,2):
        if ancho%2 == 0 and alto%2 != 0 and i >= alto-2:
            print(i, j)
            comprimida_r[i // 2].append((matriz_r[i][j] + matriz_r[i][j+1]) // 2)
            comprimida_g[i // 2].append((matriz_r[i][j] + matriz_g[i][j+1]) // 2)
            comprimida_b[i // 2].append((matriz_r[i][j] + matriz_b[i][j+1]) // 2)
        elif ancho%2 != 0 and alto%2 == 0 and j >= ancho-2:
            print(i, j)
            comprimida_r[i // 2].append((matriz_r[i][j] + matriz_r[i+1][j]) // 2)
            comprimida_g[i // 2].append((matriz_r[i][j] + matriz_g[i+1][j]) // 2)
            comprimida_b[i // 2].append((matriz_r[i][j] + matriz_b[i+1][j]) // 2)
        elif ancho%2 != 0 and alto%2 != 0 and j >= ancho - 2 and i >= alto-2:
            print(i, j)
            comprimida_r[i // 2].append(matriz_r[i][j])
            comprimida_g[i // 2].append(matriz_r[i][j])
            comprimida_b[i // 2].append(matriz_r[i][j])
        elif ancho%2 != 0 and alto%2 != 0 and j >= ancho-2:
            print(i, j)
            comprimida_r[i // 2].append((matriz_r[i][j] + matriz_r[i+1][j]) // 2)
            comprimida_g[i // 2].append((matriz_r[i][j] + matriz_g[i+1][j]) // 2)
            comprimida_b[i // 2].append((matriz_r[i][j] + matriz_b[i+1][j]) // 2)
        else:
            print(i,j)
            print(alto, ancho)
            comprimida_r[i//2].append((matriz_r[i][j]+matriz_r[i][j+1]+matriz_r[i+1][j]+matriz_r[i+1][j+1])//4)
            comprimida_g[i//2].append((matriz_g[i][j]+matriz_g[i][j+1]+matriz_g[i+1][j]+matriz_g[i+1][j+1])//4)
            comprimida_b[i//2].append((matriz_b[i][j]+matriz_b[i][j+1]+matriz_b[i+1][j]+matriz_b[i+1][j+1])//4)

######################################################################
##### FINAL DE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES ###################
######################################################################

# Mostrar estadísticas de compresión
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r, comprimida_g, comprimida_b)

# Guardar matriz comprimida
amsc.matrices_a_imagen(comprimida_r, comprimida_g, comprimida_b, ruta_imagen_comprimida)

