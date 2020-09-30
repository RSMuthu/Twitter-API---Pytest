import pytest
from conftest import twitter_session, BASE_URL

status_list = ["We welcome you to MSD family :)", "Lets have fun !!"]
#@pytest.mark.usefixtures("twitter_session")
@pytest.mark.parametrize("status_text", status_list)
def test_make_tweet(twitter_session, status_text):
    '''
    This module is to test the creation of a tweet.

    Args:
    twitter_session - the OAuth1Session from the pytest fixture.
    status_text - the text which will be dumped in the tweet created for testing.
    '''
    resp = twitter_session.post(f"{BASE_URL}/statuses/update.json", params={'status': status_text})
    print (resp.text)
    assert resp.status_code == 200
    data = resp.json()
    #tweet_id = data['id']
    #tweet_msg = data['text']
    #tweet_user = data['user']['id']
    assert data['text'] == status_text
