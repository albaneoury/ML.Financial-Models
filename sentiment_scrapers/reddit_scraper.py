import praw
import pandas as pd
from textblob import TextBlob

def scrap_reddit_with_sentiment(keywords, max_posts=30):
    reddit = praw.Reddit(
        client_id="TON_CLIENT_ID",
        client_secret="TON_CLIENT_SECRET",
        user_agent="my_scraper"
    )

    all_posts = []
    for keyword in keywords:
        for submission in reddit.subreddit("all").search(keyword, sort='new', limit=max_posts):
            text = f"{submission.title} {submission.selftext}"
            polarity = TextBlob(text).sentiment.polarity
            sentiment = (
                "positive" if polarity > 0 else
                "negative" if polarity < 0 else
                "neutral"
            )
            all_posts.append({
                'keyword': keyword,
                'content': text,
                'sentiment_score': polarity,
                'sentiment': sentiment
            })

    return pd.DataFrame(all_posts)