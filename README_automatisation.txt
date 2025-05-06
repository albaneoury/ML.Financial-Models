
README – Automatisation Scraping et Analyse de Sentiment
========================================================

📅 Automatisations prévues
---------------------------
- Tous les jours à 7h00 : Scraping des données macroéconomiques (FRED)
- Tous les jours à 8h00 : Scraping des posts Twitter, Reddit et LinkedIn + analyse de sentiment via Jupyter Notebook

📂 Dossiers utilisés
--------------------
- Données journalières : `daily_sentiment_data/`
- Données macro : `macro_geopolitical_data.csv`
- Historique des sentiments : `historical_sentiment.csv`
- Logs : dans `log_macro.txt` et `log_daily.txt` sur le bureau dans le dossier `ML project`

🛠️ Scripts automatisés via crontab
-----------------------------------
> Pour voir ou modifier :
$ crontab -e

> Lignes dans le crontab :

0 7 * * * /opt/anaconda3/bin/python3 "/Users/albane/Desktop/ML project/macro_scraper_updated.py" >> /Users/albane/Desktop/ML\ project/log_macro.txt 2>&1
0 8 * * * /opt/anaconda3/bin/python3 "/Users/albane/Desktop/ML project/daily_scraper.py" >> /Users/albane/Desktop/ML\ project/log_daily.txt 2>&1

🧪 Tester manuellement
-----------------------
> Macro :
$ python3 "/Users/albane/Desktop/ML project/macro_scraper_updated.py"

> Réseaux sociaux :
$ python3 "/Users/albane/Desktop/ML project/daily_scraper.py"

📋 Vérifier les logs
---------------------
$ cat "/Users/albane/Desktop/ML project/log_macro.txt"
$ cat "/Users/albane/Desktop/ML project/log_daily.txt"

🕵️‍♀️ Suivi
-----------
Fichier mis à jour automatiquement chaque jour. Résultats visibles dans :
- `daily_sentiment_data/` : tous les posts avec sentiments
- `historical_sentiment.csv` : toutes les données fusionnées
- `macro_geopolitical_data.csv` : données économiques clés

🗓️ Dernière mise à jour : 2025-04-10
