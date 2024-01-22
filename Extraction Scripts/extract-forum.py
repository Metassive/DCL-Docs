from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor

url = 'https://forum.decentraland.org/latest'
base_url = 'https://forum.decentraland.org'

driver = webdriver.Chrome()
driver.get(url)

def extraer_datos_post(url):
    print(url)
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    with open('forum.txt','a') as archivo:
        archivo.write(f"\n\n# URL: {url}\n\n")
        for etiqueta in soup.find_all(text=True):
            if etiqueta.parent.name not in ['script', 'style'] and etiqueta.strip():
                archivo.write(f"<{etiqueta.parent.name}>{etiqueta.strip()}</{etiqueta.parent.name}>\n")
    #with open('forum.txt','a') as f:
        

# Function to obtain the unique URLs of the threads
def obtener_urls_unicas():
    threads = driver.find_elements(By.XPATH,"//td[@class='main-link clearfix topic-list-data']")
    urls = set()  # Usamos un conjunto para almacenar URLs únicas

    for thread in threads:
        thread_url =thread.find_element(By.TAG_NAME,'a').get_attribute('href')
        urls.add(thread_url)

    return urls

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Espera a que carguen los nuevos threads

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("End of scroll, collecting URLs...")
        break

    last_height = new_height

# Get all unique URLs collected
urls_unicas = obtener_urls_unicas()
for url in urls_unicas:
    with open('forum-urls.txt','a') as f:
        f.write(url+'\n')

# Use ThreadPool with a for loop
with ThreadPoolExecutor(max_workers=1) as executor:
    for url in urls_unicas:
        executor.submit(extraer_datos_post, url)


driver.quit()  # Close the browser when finished
