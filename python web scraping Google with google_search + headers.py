#!/usr/bin/env python
# coding: utf-8

# In[1]:


from googlesearch import search
import requests
from bs4 import BeautifulSoup
import time
import random
from datetime import datetime
from fake_useragent import UserAgent
import sys
import threading

def generate_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.google.com/',
    }
    return headers

def animate_loading(start_time, stop_event):
    while not stop_event.is_set():
        elapsed_time = int(time.time() - start_time)
        minutes, seconds = divmod(elapsed_time, 60)
        sys.stdout.write(f"\rScraping des résultats de recherche Google en cours. Veuillez patienter... Temps écoulé: {minutes} minutes et {seconds} secondes")
        sys.stdout.flush()
        time.sleep(1)

def fetch_title_and_snippet(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding  # Utiliser l'encodage apparent
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Essayer de trouver le titre
        title = soup.title.string if soup.title else "N/A"
        
        # Essayer de trouver un extrait (snippet)
        snippet = " ".join(p.get_text() for p in soup.find_all('p')[:2])  # Prendre les deux premiers paragraphes
        
        return title, snippet
    except Exception as e:
        return "N/A", "N/A"

def google_search(query, max_results=10, max_duration=900):
    results = []
    try:
        start_time = time.time()
        stop_event = threading.Event()
        loading_thread = threading.Thread(target=animate_loading, args=(start_time, stop_event))
        loading_thread.start()

        # Limiter manuellement le nombre de résultats
        for i, url in enumerate(search(query)):
            if i >= max_results or (time.time() - start_time) >= max_duration:
                break
            headers = generate_headers()
            title, snippet = fetch_title_and_snippet(url, headers)
            site_name = url.split('/')[2] if '//' in url else url.split('/')[0]
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            results.append({'title': title, 'link': url, 'snippet': snippet, 'site_name': site_name, 'date': date})
            time.sleep(random.uniform(7, 11))  # Temps de pause pour chaque requête

        if (time.time() - start_time) >= max_duration:
            print("\nErreur : Le délai d'attente a été dépassé.")
            print("\nLes résultats récupérés : ")

        stop_event.set()
        loading_thread.join()  # Attendre que l'animation se termine

    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(f"\nErreur lors de la recherche Google : {e}")

    return results

if __name__ == "__main__":
    query = input('Rechercher sur le web : ')
    results = google_search(query, max_results=10, max_duration=900)  

    if results:
        print("\nRésultats de recherche Google pour : " + '"' + query + '"')

        #for result in results:
        for i, result in enumerate(results, 1):
            print(f"Résultat Google {i}:")
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Snippet: {result['snippet']}")
            print(f"Site Name: {result['site_name']}")
            print(f"Date: {result['date']}\n")

    print("FIN")

