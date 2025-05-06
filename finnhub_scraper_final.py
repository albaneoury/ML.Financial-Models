import requests
import pandas as pd
from datetime import datetime
import time

API_KEY = "cvrr821r01qnpem97l8gcvrr821r01qnpem97l90"
tickers = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

results = []
today = datetime.now().strftime("%Y-%m-%d")

for symbol in tickers:
    try:
        url = f"https://finnhub.io/api/v1/stock/metric?symbol={symbol}&metric=all&token={API_KEY}"
        response = requests.get(url)
        data = response.json()
        metrics = data.get("metric", {})

        results.append({
            "ticker": symbol,
            "date": today,
            "EPS": metrics.get("eps"),
            "ROE": metrics.get("roe"),
            "P/E": metrics.get("peBasicExclExtraTTM"),
            "Revenue/Share": metrics.get("revenuePerShare"),
            "Debt/Equity": metrics.get("debtEquityRatio"),
            "Net Margin": metrics.get("netMargin")
        })

        print(f"✅ Données récupérées pour {symbol}")
    except Exception as e:
        print(f"❌ Erreur avec {symbol} :", e)

    time.sleep(1)

df = pd.DataFrame(results)
df.to_csv(f"finnhub_financial_data_{today}.csv", index=False)
print(f"💾 Données sauvegardées dans finnhub_financial_data_{today}.csv")