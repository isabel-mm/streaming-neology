def limpiar_tweet(texto):
	texto = texto.lower() # normalizar a minúsculas
	texto = re.sub(r'@[A-Za-z0-9_]+', '', texto) # todo lo que vaya precedido de @ (usuarios)
	texto = re.sub(r'#([^\s]+)', '', texto) # todo lo que vaya precedido de # (hashtags)
	texto = re.sub(r'\d', '', texto) # eliminar dígitos
	texto = re.sub(r'\d{1,2}/\d{1,2}/\d{4}', '', texto) # formato de fecha
	texto = re.sub(r'https?://[A-Za-z0-9./]+', '', texto) # todo lo que vaya precedido de https (enlaces)
	texto = re.sub(r'[^\w\s]', '', texto) # eliminar caracteres especiales excepto espacios en blanco
	texto = re.sub(r'\s+', ' ', texto).strip() # eliminar espacios en blanco y saltos de línea
	texto = ''.join(c for c in texto if c not in emoji.EMOJI_DATA) # eliminar emojis
	texto = re.sub(r'\bjaj\w*\b', '', texto) # eliminar secuencias de risa
	texto = re.sub(r'(\w)\1{2,}', r'\1', texto)
