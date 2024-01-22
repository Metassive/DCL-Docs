# We import the re library to work with regular expressions
import re

# Function to remove <span> tags and their content
def eliminar_etiquetas_span(texto):
    texto = re.sub(r'<span.*?>.*?</span>', '', texto, flags=re.DOTALL | re.IGNORECASE)
    return texto

# Function to remove the content of <a> tags that are on individual lines
def eliminar_etiquetas_a_en_lineas(texto):
    texto = re.sub(r'^<a.*?>.*?</a>$', '', texto, flags=re.MULTILINE | re.IGNORECASE)
    return texto

# Function to remove <[document]> tags and their content
def eliminar_etiquetas_document(texto):
    texto = re.sub(r'<\[document\]>.*?</\[document\]>', '', texto, flags=re.DOTALL | re.IGNORECASE)
    return texto

# Function to remove <div> tags and their content
def eliminar_etiquetas_div(texto):
    texto = re.sub(r'<div.*?>.*?</div>', '', texto, flags=re.DOTALL | re.IGNORECASE)
    return texto

# Function to replace multiple line breaks with a single one
def reemplazar_saltos_de_linea(texto):
    texto = re.sub(r'\n+', '\n\n', texto)
    return texto

# Open the original file in reading mode
with open('docs-TEXT.txt', 'r') as archivo:
    contenido = archivo.read()

    # Use functions to remove tags and replace line breaks
    contenido = eliminar_etiquetas_span(contenido)
    contenido = eliminar_etiquetas_a_en_lineas(contenido)
    contenido = eliminar_etiquetas_document(contenido)
    contenido = eliminar_etiquetas_div(contenido)
    contenido_modificado = reemplazar_saltos_de_linea(contenido)

# Open a new file in writing mode
with open('docs-TEXT---clean.txt', 'w') as archivo:
    archivo.write(contenido_modificado)

print("The information has been processed.")
