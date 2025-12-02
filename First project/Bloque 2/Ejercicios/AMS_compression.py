from PIL import Image

def imagen_a_matrices(ruta_imagen):
    """
    Lee una imagen JPG y la convierte a tres matrices de listas 2D
    Una matriz para cada canal: R, G, B
    """
    img = Image.open(ruta_imagen)
    ancho, alto = img.size

    # Convertir a RGB si no lo es
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Obtener datos de píxeles
    pixels = list(img.getdata())

    # Crear tres matrices 2D vacías
    matriz_r = []  # Matriz para canal Rojo
    matriz_g = []  # Matriz para canal Verde
    matriz_b = []  # Matriz para canal Azul

    # Llenar las matrices
    for y in range(alto):
        fila_r = []
        fila_g = []
        fila_b = []

        for x in range(ancho):
            index = y * ancho + x
            r, g, b = pixels[index]

            fila_r.append(r)
            fila_g.append(g)
            fila_b.append(b)

        matriz_r.append(fila_r)
        matriz_g.append(fila_g)
        matriz_b.append(fila_b)

    return matriz_r, matriz_g, matriz_b, ancho, alto

def matrices_a_imagen(matriz_r, matriz_g, matriz_b, ruta_salida):
    """
    Convierte las tres matrices 2D a imagen JPG
    """
    alto = len(matriz_r)
    ancho = len(matriz_r[0])

    # Crear lista plana de píxeles combinando las tres matrices
    pixels = []
    for y in range(alto):
        for x in range(ancho):
            r = matriz_r[y][x]
            g = matriz_g[y][x]
            b = matriz_b[y][x]
            pixels.append((r, g, b))

    # Crear imagen y guardar
    img = Image.new('RGB', (ancho, alto))
    img.putdata(pixels)
    img.save(ruta_salida, 'JPEG', quality=85)

    return img

def calcular_tamano_matriz_2d(matriz):
    """Calcula el tamaño en bytes (una posición = un byte) de una matriz 2D"""
    if not matriz or not matriz[0]:
        return 0
    
    alto = len(matriz)
    ancho = len(matriz[0])
    
    return alto * ancho

def mostrar_stats(matriz_r_orig, matriz_g_orig, matriz_b_orig,
                        matriz_r_comp, matriz_g_comp, matriz_b_comp):
    """Muestra estadísticas de compresión"""
    tamano_orig = (calcular_tamano_matriz_2d(matriz_r_orig) +
                   calcular_tamano_matriz_2d(matriz_g_orig) +
                   calcular_tamano_matriz_2d(matriz_b_orig))

    tamano_comp = (calcular_tamano_matriz_2d(matriz_r_comp) +
                   calcular_tamano_matriz_2d(matriz_g_comp) +
                   calcular_tamano_matriz_2d(matriz_b_comp))

    print(f"\n=== STATS DE COMPRESION ===")
    print(f"Resolución: {len(matriz_r_orig[0])}x{len(matriz_r_orig)}")
    print(f"Tamaño estimado original: {tamano_orig} bytes")
    print(f"Tamaño estimado comprimido: {tamano_comp} bytes")

    if tamano_orig > 0:
        if tamano_comp > 0:
            ratio = tamano_orig / tamano_comp
        else:
            ratio = float('inf')
        reduccion = (1 - tamano_comp/tamano_orig) * 100
        print(f"Ratio de compresión: {ratio:.2f}x")
        print(f"Reducción: {reduccion:.2f}%")


