import sys
import os

# Ajoute le dossier courant au chemin de recherche de Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.controllers.scraping_controller import ScrapingController

if __name__ == "__main__":
    recherche = "clavier gamer"
    controleur = ScrapingController()
    controleur.lancer(recherche)