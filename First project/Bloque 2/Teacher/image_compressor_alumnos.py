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

######################################################################
##### FINAL DE TU CÓDIGO DE COMPRESIÓN DE IMÁGENES ###################
######################################################################

# Mostrar estadísticas de compresión
amsc.mostrar_stats(matriz_r, matriz_g, matriz_b, comprimida_r, comprimida_g, comprimida_b)

# Guardar matriz comprimida
amsc.matrices_a_imagen(comprimida_r, comprimida_g, comprimida_b, ruta_imagen_comprimida)

