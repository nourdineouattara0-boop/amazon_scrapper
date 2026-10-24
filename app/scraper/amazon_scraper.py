import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.scraper.driver import initialiser_driver
from app.scraper.parsing import analyser_html
from config import URL_SITE, TEMPS_ATTENTE

class AmazonScraper:
    def __init__(self):
        self.driver = initialiser_driver()

    def chercher(self, mot_cle):
        try:
            self.driver.get(URL_SITE)
            
            
            barre_recherche = WebDriverWait(self.driver, TEMPS_ATTENTE).until(
                EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
            )
            
            time.sleep(2)  # Pause humaine anti-bot
            barre_recherche.clear()
            barre_recherche.send_keys(mot_cle)
            
            bouton_valider = self.driver.find_element(By.ID, "nav-search-submit-button")
            bouton_valider.click()
            
            WebDriverWait(self.driver, TEMPS_ATTENTE).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-result-item[data-component-type='s-search-result']"))
            )
            
            time.sleep(3)  # Pause supplémentaire pour laisser charger
            html = self.driver.page_source
            return analyser_html(html)
            
        finally:
            self.driver.quit()