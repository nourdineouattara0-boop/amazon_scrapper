from app.scraper.amazon_scraper import AmazonScraper
from app.models.depot import DepotProduit
from app.views.console_view import ConsoleView
from app.views.export_view import ExportView

class ScrapingController:
    def __init__(self):
        self.depot = DepotProduit()

    def lancer(self, mot_cle):
        ConsoleView.afficher(f"Lancement de la recherche pour : '{mot_cle}'")
        
        scraper = AmazonScraper()
        liste_produits = scraper.chercher(mot_cle)
        
        for produit in liste_produits:
            self.depot.ajouter(produit)
            
        ConsoleView.afficher_resultats(self.depot.obtenir_tous())
        
        ExportView.en_csv(self.depot.obtenir_tous())
        ExportView.en_json(self.depot.obtenir_tous())
        ConsoleView.afficher("Sauvegarde CSV et JSON terminée !")