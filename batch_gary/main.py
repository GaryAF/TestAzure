#!/usr/bin/env python3
"""
Scraper Selenium - Configuration basique
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# URL à scraper
TARGET_URL = "https://www.sefair-energies.fr/"  # Remplacez par l'URL cible

def setup_driver():
    """Configure et initialise le driver Selenium"""
    chrome_options = Options()
    
    # Options de base pour l'exécution dans un container
    chrome_options.add_argument("--headless")  # Mode sans interface graphique
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # User agent standard
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Initialiser le driver
    driver = webdriver.Chrome(options=chrome_options)
    
    return driver

def main():
    """Fonction principale"""
    print("Démarrage du scraper...")
    
    # Configurer et obtenir le driver
    driver = setup_driver()
    
    try:
        # Effectuer la requête GET
        print(f"Accès à {TARGET_URL}")
        driver.get(TARGET_URL)
        
        # Attendre que la page se charge (optionnel)
        time.sleep(2)
        
        # Afficher le titre de la page pour confirmer l'accès
        print(f"Titre de la page: {driver.title}")
        
        # Ici vous pouvez ajouter le code de scraping selon vos besoins
        
    except Exception as e:
        print(f"Erreur: {e}")
    
    finally:
        # Fermer le driver
        driver.quit()
        print("Scraper terminé")

if __name__ == "__main__":
    main()