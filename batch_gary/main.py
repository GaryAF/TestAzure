#!/usr/bin/env python3
"""
Scraper Selenium - Configuration basique
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

# URL à scraper
TARGET_URL = "https://www.sefair-energies.fr/"

def setup_driver():
    """Configure et initialise le driver Selenium"""
    chrome_options = Options()
    
    # Options de base pour l'exécution dans un container
    chrome_options.add_argument("--headless")  # Mode sans interface graphique
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # Options supplémentaires pour éviter les erreurs dans le container
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-setuid-sandbox")
    
    # User agent standard
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Vérifier si nous sommes dans un environnement Docker et configurer pour Chromium
    if os.path.exists("/usr/bin/chromium"):
        print("Environnement Docker ARM détecté, utilisation de Chromium")
        chrome_options.binary_location = "/usr/bin/chromium"
        chromedriver_path = "/usr/bin/chromedriver"
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        print("Environnement local détecté")
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
        
        # Capturer une capture d'écran pour vérification
        if hasattr(driver, 'save_screenshot'):
            print("Enregistrement d'une capture d'écran...")
            os.makedirs("output", exist_ok=True)
            driver.save_screenshot("output/screenshot.png")
            print("Capture d'écran enregistrée dans output/screenshot.png")
        
    except Exception as e:
        print(f"Erreur: {e}")
        # Afficher plus de détails sur l'erreur
        import traceback
        traceback.print_exc()
    
    finally:
        # Fermer le driver
        driver.quit()
        print("Scraper terminé")

if __name__ == "__main__":
    main()