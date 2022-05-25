if __name__ == '__main__':
    import config
    import rand_query
else:
    from scripts import config
    from scripts import rand_query

from calendar import week
import tweepy
import random as rd
from datetime import timedelta, date, datetime
from time import sleep
#Get Random Date in the past week
today = date.today()
weekAgoToday = today - timedelta(days=5)

def random_date(start, end):

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds

    random_second = rd.randrange(int_delta)

    rand_date = start + timedelta(seconds=random_second)
    date_formatted = datetime.combine(rand_date, datetime.min.time())
    
    return date_formatted

def random_tweet():
    client = tweepy.Client(bearer_token=config.BEARER_TOKEN)
    query = rand_query.generateRandomQuery()
    
    response = client.search_recent_tweets(query=query, max_results=10, expansions = 'author_id', end_time=random_date(weekAgoToday, today))
    tweetsAuthors = [u['username'] for u in response.includes['users']]
    tweetsText = [tweet.text for tweet in response.data]

    test = {}

    for x,y in zip(tweetsAuthors, tweetsText):
        test[x] = y

    user, tweet = rd.choice(list(test.items()))

    return [str(user), tweet, query]