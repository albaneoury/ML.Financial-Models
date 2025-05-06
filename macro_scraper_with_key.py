import requests
import pandas as pd
from datetime import datetime

# --- Clé API FRED ---
API_KEY = "247259c65999150b56579dd44cd06436"

# --- Dictionnaire des indicateurs macro à récupérer ---
indicators = {
    "FEDFUNDS": "Taux directeur (Fed Funds Rate)",
    "CPIAUCNS": "Inflation (CPI, USA)",
    "UNRATE": "Taux de chômage (USA)",
    "DGS10": "Taux obligataire 10 ans (USA)",
    "GDP": "PIB USA",
}

# --- Requête et collecte ---
data = []
today = datetime.now().strftime("%Y-%m-%d")

for code, label in indicators.items():
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={code}&api_key={API_KEY}&file_type=json&sort_order=desc&limit=1"
    try:
        r = requests.get(url)
        json = r.json()
        last_point = json["observations"][0]
        value = last_point["value"]
        date = last_point["date"]
        data.append({
            "indicator_code": code,
            "label": label,
            "date": date,
            "value": value,
            "source": "FRED"
        })
    except Exception as e:
        print(f"Erreur avec {code} :", e)

# --- Sauvegarde CSV ---
df = pd.DataFrame(data)
df.to_csv("macro_geopolitical_data.csv", index=False)
print("✅ Données macro sauvegardées dans macro_geopolitical_data.csv")