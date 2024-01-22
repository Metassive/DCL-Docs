import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time



start_time = time.time()

exclusiones=[]
exclusiones = exclusiones or set()
exclusiones.update([
    'https://github.com/decentraland',
    'https://github.com/decentraland-scenes',
    'https://linktr.ee/decentralanddao',
    'https://wordpress.com/',
    'wordpress',
    '.png',
    '.jpg',
    '.gif',
    '.jpeg',
    '.pdf',
    '/login?',
    '/signup?',
    'https://decentraland.org/blog',
    'https://forum.decentraland.org',
    'https://peer.decentraland.org',
    'https://agora.decentraland.org',
    'https://play.decentraland.org',
    'https://governance.decentraland.org',
    'https://builder.decentraland.org',
    'https://forum.decentraland.org',
    'https://governance.decentraland.org',
    'https://builder.decentraland.org',
    'https://events.decentraland.org/',
    'https://intercom.decentraland.org/',
    'https://playground.decentraland.org',
    'https://decentraland.org/discord/',
    'https://status.decentraland.org/',
    'https://vesting.decentraland.org',
    'https://adr.decentraland.org',
    'https://ui.decentraland.org/',
    'https://contracts.decentraland.org',
    'https://studios.decentraland.org',
    '/builder',
    '/item-editor',
    'market.decentraland.org',
    'storage/contents/',


])
#IF the file with the extracted urls does not exist, it creates it empty
try:
    open("urls_extraidas.txt","r").read()
except:
    open("urls_extraidas.txt","w").write("")
    

def limpiar_spans(nombre_archivo):
    # Lee el archivo 
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    # Processes the text to combine adjacent spans with a space between each
    processed_lines = []
    combined_span = ''
    for line in lines:
        line = line.strip()
        if line.startswith('<span>'):
            combined_span += line[6:-7] + ' '  # Agrega el contenido del span sin las etiquetas y un espacio
        else:
            if combined_span:
                processed_lines.append(f'<span>{combined_span}</span>')  # Agrega el contenido combinado en un nuevo span
                combined_span = ''
            processed_lines.append(line)

    # Write the result to a new file or overwrite the file
    with open(nombre_archivo, 'w') as file:
        file.write('\n'.join(processed_lines))

def guardar_textos(url, nombre_archivo, urls_procesadas, archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para errores de solicitud HTTP
        soup = BeautifulSoup(response.text, 'html')
    except requests.exceptions.RequestException as e:
        print(f"Could not get page content '{url}': {e}")
        return
    except Exception as e:
        print(f"An error occurred while processing the page '{url}': {e}")
        return

    if not soup:
        print(f"Could not parse page structure '{url}' correctly.")
        return

    try:
        archivo.write(f"\n\n# Start of the information extracted from the URL: {url}\n\n")
        for etiqueta in soup.find_all(text=True):
            if etiqueta.parent.name not in ['script', 'style'] and etiqueta.strip():
                archivo.write(f"<{etiqueta.parent.name}>{etiqueta.strip()}</{etiqueta.parent.name}>\n")

        print(f"Page texts have been saved '{url}' in '{nombre_archivo}'.")

        for enlace in soup.find_all('a', href=True): #Recorremos un bucle por todas las URL encontradas en la URL actual
            next_url = enlace['href']
            parsed_next_url = urlparse(next_url)
            if parsed_next_url.scheme and parsed_next_url.netloc:
                exclude_url = False
                for exclusion in exclusiones:
                    if exclusion.lower() in next_url.lower():  # Verifica si la URL contiene alguna de las excluidas
                        exclude_url = True
                        break
                if not "decentraland.org" in next_url: #Omite las urls fuera del dominio de decentraland.org
                    exclude_url=True
                if exclude_url:
                    continue  # Omite la URL si contiene alguna de las excluidas
                # Code to process and save URLs
                with open('urls_extraidas.txt', 'r') as f:
                    urls_extraidas = set(f.read().splitlines())
                if next_url not in urls_extraidas:
                    with open('urls_extraidas.txt', 'a') as f:
                        f.write(f"{next_url}\n")
                    archivo.write(f"\n\n# End of the information extracted from the URL: {url}\n\n")
                    guardar_textos(next_url, nombre_archivo, urls_procesadas, archivo)
    except Exception as e:
        print(f"An error occurred while processing the page '{url}': {e}")
        return



nombre_archivo = 'docs-TEXT.txt'
urls_procesadas = set()
url = 'https://decentraland.org/'

# Open the file only once for the entire operation
with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
    # Call the function to save the content
    guardar_textos(url, nombre_archivo, urls_procesadas, archivo)

# Execute the clean spans function
limpiar_spans(nombre_archivo)



end_time = time.time()
execution_time = end_time - start_time
print(f"The program took {execution_time} seconds to finish.")