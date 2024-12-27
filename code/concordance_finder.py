import csv

# Función para leer el archivo CSV y buscar las concordancias
def buscar_concordancias(corpus_file, termino_buscar):
    # Lista para almacenar los resultados
    concordancias = []
    
    # Abrir el archivo CSV en modo lectura
    with open(corpus_file, mode='r', encoding='utf-8') as archivo:
        # Usar el lector CSV
        lector = csv.reader(archivo, delimiter=';')
        
        # Iterar sobre las filas del archivo
        for i, fila in enumerate(lector):
            # El tweet está en la primera columna (índice 0)
            tweet = fila[0]
            
            # Comprobar si el palabra de búsqueda está en el tweet
            if termino_buscar.lower() in tweet.lower():
                # Guardar el tweet junto con su número de línea
                concordancias.append((i + 1, tweet))
    
    return concordancias

# Función principal
def main():
    # Nombre del archivo CSV
    archivo_csv = 'corpus_twitter.csv'
    
    # Pedir al usuario un palabra o frase para buscar
    termino = input("Introduce la palabra o frase que deseas buscar: ").strip()
    
    # Buscar las concordancias
    concordancias = buscar_concordancias(archivo_csv, termino)
    
    # Mostrar resultados
    if concordancias:
        print(f"\nSe han encontrado {len(concordancias)} concordancias con '{termino}':\n")
        for idx, tweet in concordancias:
            print(f"Línea {idx}: {tweet}\n")
    else:
        print(f"No se encontraron concordancias para '{termino}'.")

# Ejecutar el script
if __name__ == "__main__":
    main()
