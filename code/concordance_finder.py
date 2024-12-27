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

# Función para guardar los resultados en un archivo CSV
def guardar_resultados_csv(concordancias, termino):
    nombre_archivo = f"concordancias_{termino.replace(' ', '_')}.csv"
    # Usar 'utf-8-sig' para manejar mejor los caracteres especiales y asegurarse de que Excel los lea correctamente
    with open(nombre_archivo, mode='w', encoding='utf-8-sig', newline='') as archivo_salida:
        escritor = csv.writer(archivo_salida, delimiter=';')
        # Escribir encabezado
        escritor.writerow(['Línea', 'Tweet'])
        # Escribir las concordancias
        for idx, tweet in concordancias:
            escritor.writerow([idx, tweet])
    print(f"\nLos resultados se han guardado en '{nombre_archivo}'.")

# Función principal
def main():
    # Nombre del archivo CSV
    archivo_csv = 'corpus_twitter.csv'
    
    while True:
        # Pedir al usuario una palabra o frase para buscar
        termino = input("Introduce la palabra o neologismo que quieras buscar: ").strip()
        
        # Buscar las concordancias
        concordancias = buscar_concordancias(archivo_csv, termino)
        
        # Mostrar resultados
        if concordancias:
            print(f"\nSe han encontrado {len(concordancias)} concordancias con '{termino}':\n")
            for idx, tweet in concordancias:
                print(f"Línea {idx}: {tweet}\n")
        else:
            print(f"No se encontraron concordancias para '{termino}'.")
        
        # Preguntar si desea guardar los resultados en un archivo CSV
        guardar = input("\n¿Quieres guardar los resultados en un archivo CSV? (s/n): ").strip().lower()
        if guardar == 's':
            guardar_resultados_csv(concordancias, termino)
        
        # Preguntar si desea realizar otra búsqueda
        otra_busqueda = input("\n¿Quieres realizar otra búsqueda? (s/n): ").strip().lower()
        if otra_busqueda != 's':
            print("¡Hasta luego! :-)")
            break

# Ejecutar el script
if __name__ == "__main__":
    main()
