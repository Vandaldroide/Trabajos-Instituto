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
comprimida_r = [] #matriz comprimida del canal rojo
comprimida_g = [] #matriz comprimida del canal verde
comprimida_b = [] #matriz comprimida del canal azul

csum = [0,0,0] # Cache de las sumas para la media
pixeles = input("De cuanto quieres que sea el pixel binning? ") #de cuantos pixeles es el binning
pixeles = int(pixeles)
altmodpix = alto%pixeles #Modulo del alto
anmodpix = ancho%pixeles # Modulo del ancho
for i in range(0,alto,pixeles):
    comprimida_r.append([])
    comprimida_g.append([])
    comprimida_b.append([])
    for j in range(0,ancho,pixeles):
        if anmodpix == 0 and altmodpix != 0 and i >= alto-pixeles:
            csum = [0, 0, 0]
            for k in range(altmodpix):
                for l in range(pixeles):
                    csum[0] += matriz_r[i+k][j+l]
                    csum[1] += matriz_g[i+k][j+l]
                    csum[2] += matriz_b[i+k][j+l]
            comprimida_r[i // pixeles].append(csum[0] // (pixeles*(altmodpix)))
            comprimida_g[i // pixeles].append(csum[1] // (pixeles*(altmodpix)))
            comprimida_b[i // pixeles].append(csum[2] // (pixeles*(altmodpix)))
        elif anmodpix != 0 and altmodpix == 0 and j >= ancho-pixeles:
            csum = [0, 0, 0]
            for k in range(pixeles):
                for l in range(anmodpix):
                    csum[0] += matriz_r[i+k][j+l]
                    csum[1] += matriz_g[i+k][j+l]
                    csum[2] += matriz_b[i+k][j+l]
            comprimida_r[i // pixeles].append(csum[0] // (pixeles*(anmodpix)))
            comprimida_g[i // pixeles].append(csum[1] // (pixeles*(anmodpix)))
            comprimida_b[i // pixeles].append(csum[2] // (pixeles*(anmodpix)))
        elif anmodpix != 0 and altmodpix != 0 and j >= ancho - pixeles and i >= alto-pixeles:
            csum = [0, 0, 0]
            for k in range(altmodpix):
                for l in range(anmodpix):
                    csum[0] += matriz_r[i + k][j + l]
                    csum[1] += matriz_g[i + k][j + l]
                    csum[2] += matriz_b[i + k][j + l]
            comprimida_r[i // pixeles].append(csum[0] // ((altmodpix) * (anmodpix)))
            comprimida_g[i // pixeles].append(csum[1] // ((altmodpix) * (anmodpix)))
            comprimida_b[i // pixeles].append(csum[2] // ((altmodpix) * (anmodpix)))
        elif anmodpix != 0 and altmodpix != 0 and j >= ancho-pixeles:
            csum = [0, 0, 0]
            for k in range(pixeles):
                for l in range(anmodpix):
                    csum[0] += matriz_r[i+k][j+l]
                    csum[1] += matriz_g[i+k][j+l]
                    csum[2] += matriz_b[i+k][j+l]
            comprimida_r[i // pixeles].append(csum[0] // (pixeles*(anmodpix)))
            comprimida_g[i // pixeles].append(csum[1] // (pixeles*(anmodpix)))
            comprimida_b[i // pixeles].append(csum[2] // (pixeles*(anmodpix)))

        elif anmodpix != 0 and altmodpix != 0 and i >= alto-pixeles:
            csum = [0, 0, 0]
            for k in range(altmodpix):
                for l in range(pixeles):
                    csum[0] += matriz_r[i+k][j+l]
                    csum[1] += matriz_g[i+k][j+l]
                    csum[2] += matriz_b[i+k][j+l]
            comprimida_r[i // pixeles].append(csum[0] // (pixeles*(altmodpix)))
            comprimida_g[i // pixeles].append(csum[1] // (pixeles*(altmodpix)))
            comprimida_b[i // pixeles].append(csum[2] // (pixeles*(altmodpix)))
        else:
            csum = [0,0,0]
            for k in range(pixeles):
                for l in range(pixeles):
                    csum[0] += matriz_r[i+k][j+l]
                    csum[1] += matriz_g[i+k][j+l]
                    csum[2] += matriz_b[i+k][j+l]
            comprimida_r[i//pixeles].append(csum[0]//(pixeles**2))
            comprimida_g[i//pixeles].append(csum[1]//(pixeles**2))
            comprimida_b[i//pixeles].append(csum[2]//(pixeles**2))

######################################################################
##### FINAL DE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES ###################
######################################################################

# Mostrar estadísticas de compresión
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r, comprimida_g, comprimida_b)

# Guardar matriz comprimida
amsc.matrices_a_imagen(comprimida_r, comprimida_g, comprimida_b, ruta_imagen_comprimida)

