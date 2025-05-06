import pandas as pd
from textblob import TextBlob
import tweepy

def get_tweets_from_twitter(keywords, max_results=50):
    bearer_token = "TON_BEARER_TOKEN"
    client = tweepy.Client(bearer_token=bearer_token)

    all_tweets = []
    for keyword in keywords:
        try:
            tweets = client.search_recent_tweets(
                query=keyword,
                tweet_fields=["created_at", "public_metrics", "text", "author_id", "lang"],
                max_results=min(max_results, 100)
            )

            for tweet in tweets.data:
                text = tweet.text
                polarity = TextBlob(text).sentiment.polarity
                sentiment = (
                    "positive" if polarity > 0 else
                    "negative" if polarity < 0 else
                    "neutral"
                )

                all_tweets.append({
                    'keyword': keyword,
                    'content': text,
                    'sentiment_score': polarity,
                    'sentiment': sentiment
                })
        except:
            pass

    return pd.DataFrame(all_tweets)