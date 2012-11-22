import feedparser
def get_scores():
    d = feedparser.parse('http://www.sportsnetwork.com/aspdata/clients/sportsnetwork/NFLrssscores.aspx')
    tweet_list = []
    for i in d.entries[:3]:
        tweet_list.append(i.title + " " + i.published)
    return tweet_list
