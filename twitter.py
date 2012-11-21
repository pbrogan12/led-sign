import feedparser
def get_tweets():
    d = feedparser.parse('http://api.twitter.com/1/statuses/user_timeline.rss?screen_name=jimcramer')
    tweet_list = []
    for i in d.entries[:5]:
        tweet_list.append(i.title)
    return tweet_list
