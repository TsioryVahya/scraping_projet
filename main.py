import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://www.imdb.com/chart/top"

# En-tête pour imiter un navigateur (éviter les blocages)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Étape 1 : Envoyer une requête HTTP
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi (code 200)
if response.status_code != 200:
    print("Erreur : Impossible de récupérer la page")
    exit()

# Étape 2 : Analyser le contenu HTML
soup = BeautifulSoup(response.content, "html.parser")

# Étape 3 : Trouver la liste des films
movies = soup.find_all("li", class_="ipc-metadata-list-summary-item")[:10]

# Liste pour stocker les résultats
top_10_films = []

# Étape 4 : Extraire les informations pour chaque film
for movie in movies:
    # Titre
    title_element = movie.find("h3", class_="ipc-title__text ipc-title__text--reduced")
    title = title_element.text.strip() if title_element else "N/A"

    # Année (premier élément de la metadata)
    year_element = movie.find("span", class_="sc-15ac7568-7 cCsint cli-title-metadata-item")
    year = year_element.text.strip() if year_element else "N/A"

    # Note
    rating_element = movie.find("span", class_="ipc-rating-star--rating")
    rating = rating_element.text.strip() if rating_element else "N/A"

    # Ajouter au résultat
    top_10_films.append({
        "title": title,
        "year": year,
        "rating": rating
    })

# Étape 5 : Afficher les résultats
print("Top 10 des films sur IMDb :")
for i, film in enumerate(top_10_films, 1):
    print(f"{i}. {film['title']} ({film['year']}) - Note : {film['rating']}")

# Étape 6 (facultatif) : Sauvegarder dans un fichier CSV
import csv
with open("top_10_films.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "year", "rating"])
    writer.writeheader()
    writer.writerows(top_10_films)