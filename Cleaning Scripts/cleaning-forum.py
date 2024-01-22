import re

def eliminar_etiquetas_span(texto):
    return re.sub(r'<span.*?>.*?</span>', '', texto, flags=re.DOTALL | re.IGNORECASE)

def eliminar_etiquetas_a_en_lineas(texto):
    return re.sub(r'^<a.*?>.*?</a>$', '', texto, flags=re.MULTILINE | re.IGNORECASE)

def eliminar_etiquetas_document(texto):
    return re.sub(r'<\[document\]>.*?</\[document\]>', '', texto, flags=re.DOTALL | re.IGNORECASE)

def eliminar_etiquetas_div(texto):
    return re.sub(r'<div.*?>.*?</div>', '', texto, flags=re.DOTALL | re.IGNORECASE)

def eliminar_etiquetas_time(texto):
    return re.sub(r'<time.*?>.*?</time>', '', texto, flags=re.DOTALL | re.IGNORECASE)

def reemplazar_saltos_de_linea(texto):
    return re.sub(r'\n+', '\n\n', texto)

with open('forum-TEXT.txt', 'r', encoding='ISO-8859-1') as archivo:
    contenido = archivo.read()

contenido = eliminar_etiquetas_span(contenido)
contenido = eliminar_etiquetas_a_en_lineas(contenido)
contenido = eliminar_etiquetas_document(contenido)
contenido = eliminar_etiquetas_div(contenido)
contenido = eliminar_etiquetas_time(contenido)
contenido_modificado = reemplazar_saltos_de_linea(contenido)

partes = contenido_modificado.split('\n\n')
num_partes = 3
tamanio_parte = len(partes) // num_partes
partes_divididas = [partes[i:i + tamanio_parte] for i in range(0, len(partes), tamanio_parte)]

# Make sure only three files are created
partes_divididas = partes_divididas[:num_partes]

for i, parte in enumerate(partes_divididas, start=1):
    with open(f'forum-TEXT-0{i}---clean.txt', 'w', encoding='utf-8') as archivo:
        archivo.write('\n\n'.join(parte))

print("The information has been processed.")
