from selenium import webdriver
from selenium.webdriver.common.by import By
from textblob import TextBlob
import time
import pandas as pd

def scrap_linkedin_with_sentiment(keywords):
    driver = webdriver.Chrome()
    results = []

    driver.get("https://www.linkedin.com/login")
    print("👉 Connecte-toi manuellement à LinkedIn puis appuie sur ENTRÉE ici.")
    input()

    for keyword in keywords:
        print(f"🔍 Scraping pour : {keyword}")
        search_url = f"https://www.linkedin.com/search/results/content/?keywords={keyword.replace(' ', '%20')}&origin=GLOBAL_SEARCH_HEADER"
        driver.get(search_url)
        time.sleep(5)

        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

        posts = driver.find_elements(By.XPATH, '//div[contains(@class, "update-components-text")]')

        for p in posts:
            text = p.text.strip()
            if text:
                polarity = TextBlob(text).sentiment.polarity
                sentiment = (
                    "positive" if polarity > 0 else
                    "negative" if polarity < 0 else
                    "neutral"
                )
                results.append({
                    'keyword': keyword,
                    'content': text,
                    'sentiment_score': polarity,
                    'sentiment': sentiment
                })

    driver.quit()
    return pd.DataFrame(results)