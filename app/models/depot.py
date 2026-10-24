class DepotProduit:
    def __init__(self):
        self.liste_produits = []

    def ajouter(self, produit):
        self.liste_produits.append(produit)

    def obtenir_tous(self):
        return self.liste_produits