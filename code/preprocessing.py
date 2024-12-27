import os
import re
import emoji

def limpiar_tweet(texto):
    texto = texto.lower()  # normalizar a minúsculas
    texto = re.sub(r'@[A-Za-z0-9_]+', '', texto)  # todo lo que vaya precedido de @ (usuarios)
    texto = re.sub(r'#([^\s]+)', '', texto)  # todo lo que vaya precedido de # (hashtags)
    texto = re.sub(r'\d', '', texto)  # eliminar dígitos
    texto = re.sub(r'\d{1,2}/\d{1,2}/\d{4}', '', texto)  # formato de fecha
    texto = re.sub(r'https?://[A-Za-z0-9./]+', '', texto)  # todo lo que vaya precedido de https (enlaces)
    texto = re.sub(r'[^\w\s]', '', texto)  # eliminar caracteres especiales excepto espacios en blanco
    texto = re.sub(r'\s+', ' ', texto).strip()  # eliminar espacios en blanco y saltos de línea
    texto = ''.join(c for c in texto if c not in emoji.EMOJI_DATA)  # eliminar emojis
    texto = re.sub(r'\bjaj\w*\b', '', texto)  # eliminar secuencias de risa (jaja, haha, jsjs, etc.)
    texto = re.sub(r'(\w)\1{2,}', r'\1', texto)  # eliminar caracteres repetidos (por ejemplo: looool -> lol)
    return texto

def procesar_corpus():
    # Obtener todos los archivos de texto en el directorio actual
    archivos = [f for f in os.listdir() if f.endswith('.txt')]
    
    for archivo in archivos:
        with open(archivo, 'r', encoding='utf-8') as f:
            texto = f.read()
            texto_limpio = limpiar_tweet(texto)
        
        # Guardar el texto limpio de vuelta en el archivo o en un nuevo archivo
        with open(f"limpio_{archivo}", 'w', encoding='utf-8') as f:
            f.write(texto_limpio)

# Llamar a la función para procesar todos los archivos
procesar_corpus()
