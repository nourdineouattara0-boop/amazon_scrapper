class Produit:
    def _init_(self, titre, prix, url):
        self.titre = titre
        self.prix = prix
        self.url = url

    def to_dict(self):
        return {
            "titre": self.titre,
            "prix": self.prix,
            "url": self.url
        }