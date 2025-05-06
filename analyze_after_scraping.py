import os
import glob
import papermill as pm
from datetime import datetime

# Répertoire où les CSV scrappés sont stockés
save_dir = "daily_sentiment_data"
today = datetime.now().strftime('%Y-%m-%d')

# Notebooks par plateforme
notebooks = {
    "twitter": "sentiment_twitter.ipynb",
    "reddit": "sentiment_reddit.ipynb",
    "linkedin": "sentiment_linkedin.ipynb"
}

# Exécute chaque notebook avec les bons paramètres
for platform, notebook in notebooks.items():
    input_file = f"{save_dir}/{platform}_{today}.csv"
    output_notebook = f"executed_{platform}_{today}.ipynb"
    output_file = f"{save_dir}/{platform}_{today}_enriched.csv"
    
    if os.path.exists(input_file):
        print(f"📊 Analyse de sentiment {platform} lancée...")
        pm.execute_notebook(
            notebook,
            output_notebook,
            parameters=dict(input_csv=input_file, output_csv=output_file)
        )
        print(f"✅ Fichier enrichi : {output_file}")
    else:
        print(f"⚠️ Aucun fichier {input_file} trouvé.")