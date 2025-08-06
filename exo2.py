import requests
from bs4 import BeautifulSoup
import csv
import time

# Liste pour stocker tous les livres
books = []

# URL de base pour la pagination
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# En-tête pour imiter un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Boucle pour parcourir toutes les pages (1 à 50)
for page in range(1, 51):  # 50 pages pour 1000 livres (20 livres par page)
    # Construire l'URL de la page
    current_url = base_url.format(page)
    print(f"Scraping page {page}: {current_url}")
    
    # Étape 1 : Envoyer une requête HTTP
    try:
        response = requests.get(current_url, headers=headers)
        
        # Vérifier si la requête a réussi
        if response.status_code != 200:
            print(f"Erreur : Impossible de récupérer la page {current_url} (code {response.status_code})")
            continue
        
        # Étape 2 : Analyser le contenu HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Étape 3 : Trouver tous les livres sur la page
        book_elements = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
        # Vérifier si des livres sont trouvés
        if not book_elements:
            print(f"Aucun livre trouvé sur la page {page}")
            continue
        
        # Étape 4 : Extraire les informations pour chaque livre
        for book in book_elements:
            # Titre
            title_element = book.find("h3").find("a")
            title = title_element["title"].strip() if title_element and "title" in title_element.attrs else "N/A"
            
            # Prix
            price_element = book.find("p", class_="price_color")
            price = price_element.text.strip() if price_element else "N/A"
            
            # Note (convertir la classe star-rating en nombre d'étoiles)
            rating_element = book.find("p", class_="star-rating")
            rating = rating_element["class"][1] if rating_element and len(rating_element["class"]) > 1 else "N/A"
            rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = rating_dict.get(rating, "N/A")
            
            # Disponibilité
            availability_element = book.find("p", class_="instock availability")
            availability = availability_element.text.strip() if availability_element else "N/A"
            
            # Ajouter au résultat
            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability
            })
        
        # Pause pour éviter de surcharger le serveur
        time.sleep(1)
        
    except Exception as e:
        print(f"Erreur sur la page {page}: {str(e)}")
        continue

# Étape 5 : Sauvegarder dans un fichier CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "price", "rating", "availability"])
    writer.writeheader()
    writer.writerows(books)

print(f"Scraping terminé. {len(books)} livres sauvegardés dans books.csv")