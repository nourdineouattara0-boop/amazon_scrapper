from bs4 import BeautifulSoup
from app.models.produit import Produit

def analyser_html(code_html):
    soup = BeautifulSoup(code_html, 'html.parser')
    produitstrouves = []
    
    elements = soup.find_all("div", {"data-asin": True})
    
    for element in elements:
        try:
            titre_tag = element.select_one("h2 span")
            titre = titre_tag.text.strip() if titre_tag else "Titre non trouvé"
            
            prix_tag = element.select_one("span.a-price-whole")
            prix = prix_tag.text.strip() if prix_tag else "Prix non disponible"
            
            lien_tag = element.select_one("h2 a")
            url = "https://www.amazon.fr" + lien_tag['href'] if lien_tag and 'href' in lien_tag.attrs else "#"
            
            un_produit = Produit(titre=titre, prix=prix, url=url)
            produitstrouves.append(un_produit)
        except Exception:
            continue
            
    return produitstrouves