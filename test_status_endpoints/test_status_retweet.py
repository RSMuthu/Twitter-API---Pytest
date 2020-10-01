import pytest
from conftest import twitter_session, BASE_URL
from utils import get_home_tweets, get_my_retweets

@pytest.mark.run(order=2)
def test_make_retweet(twitter_session):
    '''
    Test Case for the making retweet.

    Args:
    twitter_session - the OAuth1Session from the pytest fixture.
    '''
    # get the latest tweet from our home timeline
    tweet = get_home_tweets(twitter_session, tweet_count=1)[0]
    # use the tweet id to retweet
    resp = twitter_session.post(f"{BASE_URL}/statuses/retweet/{tweet['id']}.json")
    print (f"\nRetweet Response - {resp.json()}") ## response shall be captured from std
    # Assert to confirm if the retweet made successfully
    assert resp.status_code == 200

@pytest.mark.run(order=3)
def test_undo_retweet(twitter_session):
    '''
    Test Case for the undoing the retweet.
    This test case is executed after making retweet.
    We will be searching for the retweets of self and undoing retweet.

    Args:
    twitter_session - the OAuth1Session from the pytest fixture.
    '''
    # get the latest retweet made
    tweet = get_my_retweets(twitter_session, tweet_count=1)[0]
    ## verify if its the same tweet we had made
    resp = twitter_session.post(f'{BASE_URL}/statuses/unretweet/{tweet["id"]}.json')
    print (f"\nUnretweet Response - {resp.json()}") ## response shall be captured from std
    # Assert to confirm if the unretweet made successfully
    assert resp.status_code == 200
