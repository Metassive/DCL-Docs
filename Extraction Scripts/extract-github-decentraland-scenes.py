import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time



start_time = time.time()

exclusiones=[]
exclusiones = exclusiones or set()
exclusiones.update([
    'https://linktr.ee/decentralanddao',
    'https://wordpress.com/',
    'wordpress',
    'followers',
    "people",
    'packages',
    'discussions',
    'projects',
    'report',
    'twitter',
    'topics',
    'contact',
    'decentraland.org/',
    'search',
    'decentraland-bot',
    '.png',
    '.jpg',
    '.gif',
    '.jpeg',
    '.pdf',
    '/login?',
    '/signup?',
    'issues',
    'actions',
    'projects',
    'security',
    'insights',
    'pulls',
    'storage/contents/',


])
#IF the file with the extracted urls does not exist, it creates it empty
try:
    open("urls_extraidas.txt","r").read()
except:
    open("urls_extraidas.txt","w").write("")
    

def limpiar_spans(nombre_archivo):
    # Read the file
    with open(nombre_archivo, 'r') as file:
        lines = file.readlines()

    # Processes the text to combine adjacent spans with a space between each
    processed_lines = []
    combined_span = ''
    for line in lines:
        line = line.strip()
        if line.startswith('<span>'):
            combined_span += line[6:-7] + ' '  # Add the content of the span without the tags and a space
        else:
            if combined_span:
                processed_lines.append(f'<span>{combined_span}</span>')  # Add the combined content into a new span
                combined_span = ''
            processed_lines.append(line)

    # Write the result to a new file or overwrite the file
    with open(nombre_archivo, 'w') as file:
        file.write('\n'.join(processed_lines))

def guardar_textos(url, nombre_archivo, urls_procesadas, archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Throw an exception for HTTP request errors
        soup = BeautifulSoup(response.text, 'html')
        open("test.txt","w").write(str(response.content))
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
        archivo.write(f"\n\n# URL: {url}\n\n")
        for etiqueta in soup.find_all(text=True):
            if etiqueta.parent.name not in ['script', 'style'] and etiqueta.strip():
                archivo.write(f"<{etiqueta.parent.name}>{etiqueta.strip()}</{etiqueta.parent.name}>\n")

        print(f"Page texts have been saved '{url}' in '{nombre_archivo}'.")
       
        for enlace in soup.find_all('a', href=True): #Loop through all URLs found in the current URL
            
            next_url = enlace['href']
            
            parsed_next_url = urlparse(next_url)
            #next_url="https://github.com"+next_url
            if not (parsed_next_url.scheme and parsed_next_url.netloc):
                next_url="https://github.com"+next_url
                parsed_next_url=urlparse(next_url)
            next_url=next_url.replace("#","/")
            if parsed_next_url.scheme and parsed_next_url.netloc:
                
                exclude_url = False
                
                for exclusion in exclusiones:
                    if exclusion.lower() in next_url.lower():  # Check if the URL contains any of the excluded ones
                        exclude_url = True
                        print(exclusion)
                        print(next_url)
                        print("-----------------")
                        
                        break

                
                if (not "decentraland" in next_url) or not "github" in next_url: #Ignore urls outside the domain of github.com/decentraland
                    exclude_url=True
                    
                
                
                if (not "orgs" in next_url) and (len(next_url.split("/"))>5):#Skip the content of the files, to extract only the readme
                    exclude_url=True  
                
                
                if exclude_url:
                    continue  # Skip the URL if it contains any of the excluded ones
                
                
                # Code to process and save URLs
                with open('urls_extraidas.txt', 'r') as f:
                    urls_extraidas = set(f.read().splitlines())
                if next_url not in urls_extraidas:
                    with open('urls_extraidas.txt', 'a') as f:
                        f.write(f"{next_url}\n")
                    archivo.write(f"\n\n# Change to URL: {next_url}\n\n")
                    guardar_textos(next_url, nombre_archivo, urls_procesadas, archivo)
    except Exception as e:
        print(f"An error occurred while processing the page '{url}': {e}")
        return



nombre_archivo = 'github-decentraland-scenes.txt'
urls_procesadas = set()
url = 'https://github.com/decentraland-scenes'

# Open the file only once for the entire operation
with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
    # Llamar a la función para guardar el contenido
    guardar_textos(url, nombre_archivo, urls_procesadas, archivo)

# Execute the clean spans function
limpiar_spans(nombre_archivo)



end_time = time.time()
execution_time = end_time - start_time
print(f"The program took {execution_time} seconds to finish.")