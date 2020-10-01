import pytest
from conftest import twitter_session, BASE_URL
from utils import get_home_tweets

# status list to tweet
status_list = {"We welcome you to MSD family :)", "Hello World !!"}

@pytest.mark.run(order=1) ## ording test cases -- make tweet first as first test case
@pytest.mark.parametrize("status_text", status_list) ## making it parametrized with the iterable "status text"
def test_make_tweet(twitter_session, status_text):
    '''
    Test Case for the creation of a tweet.

    Args:
    twitter_session - the OAuth1Session from the pytest fixture.
    status_text - the text which will be dumped in the tweet created for testing.
    '''
    # making API call to post the tweet with the status_text provide
    resp = twitter_session.post(f"{BASE_URL}/statuses/update.json", params={'status': status_text})
    print (f"\nTweet Response - {resp.text}") ## response shall be captured from std
    # Assert to confirm if the tweet is made successfully
    assert resp.status_code == 200
    # Assert to Confirm if the tweet made is having correct data
    assert resp.json()['text'] == status_text

@pytest.mark.run(order=4) ## ordering test cases -- delete the tweet after all the test cases are done
def test_delete_tweet(twitter_session):
    '''
    Test Case for the deletion of a tweet.
    This test case is executed post creation.
    We will be searching for the tweet from the home timeline and deleting it.

    Args:
    twitter_session - the OAuth1Session from the pytest fixture.
    '''
    # loop through the tweets made as part of test case
    for tweet in get_home_tweets(twitter_session, tweet_count=len(status_list)):
        # verifing if its the same tweet we had made, before deleting
        if tweet['text'] in status_list:
            # API call to delete the tweet
            resp = twitter_session.post(f"{BASE_URL}/statuses/destroy/{tweet['id']}.json")
            print (f"\nDelete tweet Response - {resp.text}") ## response shall be captured from std
            # Assert to confirm if the request made successfully
            assert resp.status_code == 200
