class ConsoleView:
    @staticmethod
    def afficher(message):
        print(f"[INFO] {message}")

    @staticmethod
    def afficher_resultats(produits):
        print(f"\n--- {len(produits)} PRODUITS TROUVÉS ---")
        for i, p in enumerate(produits, 1):
            print(f"{i}. {p.titre}")
            print(f"   Prix : {p.prix} €")
            print(f"   Lien : {p.url}\n")