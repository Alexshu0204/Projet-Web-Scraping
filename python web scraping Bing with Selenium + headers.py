#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import random
import time
import threading
import sys
from fake_useragent import UserAgent

def generate_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.bing.com/',
    }
    return headers

def extract_site_name(url):
    domain = urlparse(url).netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain.split('.')[0].capitalize()

def extract_snippet(result):
    try:
        snippet_element = result.find_element(By.XPATH, './/p')
        return snippet_element.text if snippet_element else 'N/A'
    except Exception:
        return 'N/A'

def parse_result(result):
    try:
        title = result.find_element(By.TAG_NAME, 'h2').text
        link = result.find_element(By.TAG_NAME, 'a').get_attribute('href')
        snippet = extract_snippet(result)
        site_name = extract_site_name(link)
        return {'title': title, 'link': link, 'snippet': snippet, 'site_name': site_name}
    except Exception as e:
        print(f"Erreur lors de l'extraction des informations : {e}")
        return None

def bing_search_selenium(query, max_results=10, timeout=599, progress_callback=None):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    #attention à bien mettre l'emplacement du fichier chromedriver.exe
    driver_path = 'C:\\chromedriver\\chromedriver-win64\\chromedriver.exe'

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    results = []
    page = 1
    start_time = time.time()
    try:
        while len(results) < max_results:
            headers = generate_headers()
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": headers['User-Agent']})
            driver.get(f'https://www.bing.com/search?q={query.replace(" ", "+")}&first={page}')
            time.sleep(random.uniform(11, 14))

            # Exclure les résultats sponsorisés en utilisant un XPath spécifique
            search_results = driver.find_elements(By.XPATH, '//li[@class="b_algo" and not(ancestor::div[contains(@class, "b_ad")])]')
            
            page_results = [parse_result(result) for result in search_results]
            results.extend([result for result in page_results if result])

            page += 10
            
            if progress_callback:
                progress_callback(len(results), max_results)

            if time.time() - start_time > timeout:
                return "Erreur : Le délai d'attente a été dépassé."
            
    finally:
        driver.quit()
    
    return results[:max_results]

def animate_loading():
    start_time = time.time()
    while not stop_animation:
        for i in range(4):
            if stop_animation:
                break
            elapsed_time = int(time.time() - start_time)
            minutes, seconds = divmod(elapsed_time, 60)
            sys.stdout.write(f"\rScraping des résultats de recherche Bing en cours. Veuillez patienter{'.' * i}{' ' * (3 - i)} Temps écoulé: {minutes} minutes et {seconds} secondes")
            sys.stdout.flush()
            time.sleep(0.5)
    elapsed_time = int(time.time() - start_time)
    minutes, seconds = divmod(elapsed_time, 60)
    sys.stdout.write(f"\rScraping des résultats de recherche Bing en cours. Veuillez patienter... Terminé! Temps écoulé: {minutes} minutes et {seconds} secondes\n")

def update_progress(current, total):
    sys.stdout.write(f"\rProgression: {current}/{total} résultats récupérés")
    sys.stdout.flush()

def run_search(query, max_results=10, timeout=599):
    results = []
    error_message = "Erreur : Le délai d'attente a été dépassé."
    
    def search():
        nonlocal results
        results = bing_search_selenium(query, max_results, timeout, progress_callback=update_progress)
    
    search_thread = threading.Thread(target=search)
    search_thread.start()
    
    start_time = time.time()
    while search_thread.is_alive():
        elapsed_time = int(time.time() - start_time)
        if elapsed_time > timeout:
            return error_message
        time.sleep(1)
    
    search_thread.join()
    
    return results

if __name__ == "__main__":
    query = input("Rechercher sur le web : ")
    
    stop_animation = False
    animation_thread = threading.Thread(target=animate_loading)
    animation_thread.start()
    
    # Exécuter la fonction avec un délai d'attente
    timeout = 599  # délai d'attente en secondes
    results = run_search(query, max_results=10, timeout=timeout)
    
    stop_animation = True
    animation_thread.join()

    if results == "Erreur : Le délai d'attente a été dépassé.":
        print(results)
    else:
        print("\nRésultats de recherche suivants : " + '"' + query + '"')
        
        for i, result in enumerate(results, 1):
            print(f"Résultat Bing {i}:")
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Snippet: {result['snippet']}")
            print(f"Site Name: {result['site_name']}\n")
        
        print("FIN")

