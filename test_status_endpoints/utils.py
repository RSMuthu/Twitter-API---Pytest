from conftest import BASE_URL

def get_home_tweets(sess, tweet_count=None):
    '''
    Helper method.
    Gets the tweets in the home_timeline of the authorized user

    Args:
    sess - the OAuth1 session
    tweet_count - number of tweet to fetch from the home timeline of the authenticated person
    '''
    # building parameter for the API call based on the tweet_count
    if not tweet_count: param = {}
    else: param = {'count' : tweet_count}
    # API call to get the tweets in the home timeline
    tweets = sess.get(f'{BASE_URL}/statuses/home_timeline.json', params=param)
    print (f"\nTweets from home_timeline Response - {tweets.text}") ## response shall be captured from std
    # Assert to confirm if the request made successfully
    assert tweets.status_code == 200
    # return the tweets (in json format) after successful retrieval
    return tweets.json()

def get_my_retweets(sess, tweet_count=None):
    '''
    Helper method.
    Gets the retweets of the authorized user

    Args:
    sess - the OAuth1 session
    tweet_count - number of tweet to fetch from the home timeline of the authenticated person
    '''
    # building parameter for the API call based on the tweet_count
    if not tweet_count: param = {}
    else: param = {'count' : tweet_count}
    # API call to get the retweets of self
    retweets = sess.get(f'{BASE_URL}/statuses/retweets_of_me.json', params=param)
    print (f"\nRetweets of user Response - {retweets.text}") ## response shall be captured from std
    # Assert to confirm if the request made successfully
    assert retweets.status_code == 200
    # return the tweets (in json format) after successful retrieval
    return retweets.json()
