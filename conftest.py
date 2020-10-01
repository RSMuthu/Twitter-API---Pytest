import pytest, json
from requests_oauthlib import OAuth1Session

BASE_URL = "https://api.twitter.com/1.1" ## base URL for Twitter API communication
## We will be using Twitter API 1.1 for the API activities

def __load_tokens():
    '''
    private method not to be used outside this module
    helps to load the access tokens for the user to work on Twitter API
    '''
    with open("tokens.json", 'r') as f_read:
        return json.load(f_read)

@pytest.fixture(scope="session") # fixture scope is for this session
def twitter_session():
    '''
    Load the session with user credentials -- access tokens.

    Authentication method available:
    Oauth1 - Oauth 1.0a has access to multiple endpoints including WRITE ops
    Oauth2 - auth bearer header only has read access

    As we will be needing to access endpoint for "statuses" WRITE operations,
    Oauth1 session is created and used for futher for all the test cases.
    '''
    tokens = __load_tokens()
    session = OAuth1Session(tokens['api_key'], client_secret=tokens['api_secret_key'],
                            resource_owner_key=tokens['access_token'],
                            resource_owner_secret=tokens['access_token_secret'])
    # OAuth1 is used for the Authentication
    return session

@pytest.fixture(scope="session")
def user_data(twitter_session):
    '''
    Verify the credentials provided for the OAuth1 session and fetch the username (screen_name)
    endpoint used - /account/verify_credentials
    '''
    resp = twitter_session.get(f"{BASE_URL}/account/verify_credentials.json")
    assert resp.status_code == 200
    # after credentials verifications return the user data as fixture
    return resp.json()
