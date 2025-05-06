# financial_scraper_finnhub.py

import requests
import pandas as pd
from datetime import datetime

api_key = "cvrr821r01qnpem97l8gcvrr821r01qnpem97l90"
tickers = ["AAPL", "GOOG", "MSFT", "TSLA", "AMZN"]
today = datetime.today().strftime("%Y-%m-%d")
output_file = f"financial_data_{today}.csv"

def get_finnhub_data(symbol):
    base = "https://finnhub.io/api/v1"
    try:
        profile = requests.get(f"{base}/stock/profile2?symbol={symbol}&token={api_key}").json()
        metrics = requests.get(f"{base}/stock/metric?symbol={symbol}&metric=all&token={api_key}").json().get("metric", {})

        return {
            "symbol": symbol,
            "companyName": profile.get("name"),
            "marketCap": metrics.get("marketCapitalization"),
            "peRatio": metrics.get("peNormalizedAnnual"),
            "eps": metrics.get("epsNormalizedAnnual"),
            "roe": metrics.get("roeAnnual"),
            "debtToEquity": metrics.get("totalDebt/totalEquityAnnual"),
            "revenueGrowth": metrics.get("revenueGrowthAnnual"),
            "date": today
        }

    except Exception as e:
        print(f"❌ Erreur pour {symbol} : {e}")
        return {}

results = [get_finnhub_data(ticker) for ticker in tickers if get_finnhub_data(ticker)]
df = pd.DataFrame(results)
df.to_csv(output_file, index=False)
print(f"📁 Données sauvegardées dans {output_file}")