import csv
import json

class ExportView:
    @staticmethod
    def en_csv(produits, fichier="exports/produits.csv"):
        with open(fichier, mode='w', newline='', encoding='utf-8') as f:
            ecrivain = csv.writer(f)
            ecrivain.writerow(["Titre", "Prix", "URL"])
            for p in produits:
                ecrivain.writerow([p.titre, p.prix, p.url])

    @staticmethod
    def en_json(produits, fichier="exports/produits.json"):
        donnees = [p.to_dict() for p in produits]
        with open(fichier, mode='w', encoding='utf-8') as f:
            json.dump(donnees, f, ensure_ascii=False, indent=4)