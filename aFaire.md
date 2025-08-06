🔰 Niveau 1 – Débutant
🎯 Objectifs :
Faire des requêtes HTTP (requests)

Extraire du HTML (BeautifulSoup)

Manipuler les balises et classes CSS

🔹 Exercice 1 : Scraper les titres de films
Site : https://www.imdb.com/chart/top

But : Extraire le Top 10 des films avec titre + année + note

🔹 Exercice 2 : Récupérer les livres
Site : http://books.toscrape.com/

But : Pour chaque livre d’une page, extraire :

Titre

Prix

Disponibilité

URL de l’image

🧭 Niveau 2 – Intermédiaire
🎯 Objectifs :
Naviguer entre plusieurs pages (pagination)

Nettoyer et structurer les données

Stocker en CSV ou JSON

🔹 Exercice 3 : Tous les livres de toutes les pages
Site : http://books.toscrape.com/

But : Scraper tous les livres du site (+1000) et stocker les infos dans un fichier CSV.

🔹 Exercice 4 : Scraper des citations
Site : http://quotes.toscrape.com/

But :

Extraire les citations, auteurs, tags

Naviguer sur plusieurs pages

🧪 Niveau 3 – Confirmé
🎯 Objectifs :
Identifier les patterns HTML complexes

Gérer les headers, cookies, et user-agents

Gérer les erreurs (404, 403, etc.)

🔹 Exercice 5 : Scraper une boutique e-commerce
Site : https://webscraper.io/test-sites/e-commerce/static

But :

Catégories → Produits

Infos produits : nom, prix, description

Pagination

🔹 Exercice 6 : Actualités technologiques
Site : https://techcrunch.com/

But :

Extraire les 5 derniers articles

Infos : titre, auteur, date, résumé

🧠 Niveau 4 – Avancé / Pro
🎯 Objectifs :
Utiliser Selenium ou Playwright pour gérer le JavaScript

Gérer les captchas / scroll infini / login

Scraper des données dynamiques ou sur demande

🔹 Exercice 7 : Site dynamique avec JavaScript
Site : https://www.airbnb.com/s/Madagascar/homes

But :

Extraire les titres, prix, notes

Scroller automatiquement pour charger plus de résultats

Besoin de Selenium ou Playwright

🔹 Exercice 8 : Scraper LinkedIn (simulation)
⚠️ Ne pas scraper le vrai LinkedIn sans API

Utilise un clone local / HTML statique

But :

Simuler un login

Extraire les profils de résultats de recherche (nom, poste, entreprise)

📂 Bonus : Sauvegarde & Analyse
Exporter les données en CSV / Excel

Les importer avec Pandas pour faire une petite analyse

Ex : prix moyen, mots-clés fréquents, etc.

📚 Conseils
🔍 Utilise SelectorGadget ou DevTools pour cibler les bons éléments

🛠️ Libs utiles : requests, beautifulsoup4, lxml, pandas, selenium, playwright

📜 Respecte les conditions d'utilisation et le robots.txt