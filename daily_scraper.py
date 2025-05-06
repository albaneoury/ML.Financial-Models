from twitter_scraper import get_tweets_from_twitter
from reddit_scraper import scrap_reddit_with_sentiment
from linkedin_scraper import scrap_linkedin_with_sentiment

from datetime import datetime
import os
import pandas as pd
import subprocess
import glob

keywords = ["S&P 500", "NASDAQ", "Apple stock", "AAPL"]
today = datetime.now().strftime('%Y-%m-%d')
save_dir = "daily_sentiment_data"
os.makedirs(save_dir, exist_ok=True)

# --- Twitter ---
try:
    df_twitter = get_tweets_from_twitter(keywords)
    df_twitter["source"] = "twitter"
    df_twitter["date"] = today
    df_twitter.to_csv(f"{save_dir}/twitter_{today}.csv", index=False)
    print(f"✅ Twitter scraped: {len(df_twitter)} posts")
except Exception as e:
    print("❌ Twitter scraping failed:", e)

# --- Reddit ---
try:
    df_reddit = scrap_reddit_with_sentiment(keywords)
    df_reddit["source"] = "reddit"
    df_reddit["date"] = today
    df_reddit.to_csv(f"{save_dir}/reddit_{today}.csv", index=False)
    print(f"✅ Reddit scraped: {len(df_reddit)} posts")
except Exception as e:
    print("❌ Reddit scraping failed:", e)

# --- LinkedIn ---
try:
    df_linkedin = scrap_linkedin_with_sentiment(keywords)
    df_linkedin["source"] = "linkedin"
    df_linkedin["date"] = today
    df_linkedin.to_csv(f"{save_dir}/linkedin_{today}.csv", index=False)
    print(f"✅ LinkedIn scraped: {len(df_linkedin)} posts")
except Exception as e:
    print("❌ LinkedIn scraping failed:", e)

# --- Fusion automatique de tous les fichiers CSV ---
def fusionner_fichiers(dossier, fichier_final):
    fichiers = glob.glob(f"{dossier}/*.csv")
    df_all = pd.concat([pd.read_csv(f) for f in fichiers if os.path.isfile(f)], ignore_index=True)
    df_all.drop_duplicates(subset=["keyword", "content", "source", "date"], inplace=True)
    df_all.to_csv(fichier_final, index=False)
    print(f"🧩 Fusion terminée : {len(df_all)} lignes sauvegardées dans {fichier_final}")

fusionner_fichiers(save_dir, "historical_sentiment.csv")

# --- Notification macOS ---
def send_notification(message, title="Scraping terminé 🧹"):
    subprocess.run([
        "osascript", "-e",
        f'display notification "{message}" with title "{title}"'
    ])

send_notification("Les données Twitter, Reddit et LinkedIn ont bien été sauvegardées ! 🚀")