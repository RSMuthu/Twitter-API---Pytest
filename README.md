# Twitter_API-Pytest

Application developers should also be in good terms with testing different
endpoints of different services/REST APIs that one builds for the work.
This is to demo a little work on unit testing Twitter API using pytest package of python.
As the unit testing task is basic, I am not writing any new pytest plugins for the purpose and just using the existing plugins.

### Task List
The task is a simple and as follows:

- Make a new tweet with the text "We welcome you to MSD family :)"
Now retweet the same tweet.
- Now get the retweet count & retweeters ID and validate the correctness of the data.
- Now revert the previous retweet (un-retweet the above tweet) and get the retweet count & retweeters ID and validate the correctness of the data.
- Now finally delete the tweet.

### Design
The design for the test cases with intent to perform above task can be either,
- __*Behaviour Driven Testing (BDD)*__
- Test case execution on our __*given specific order*__.

To ease the work, I am preferring to order the test cases based on the task / dependency.\
##### Directory structure layout
A seperate extra directory (for each module) outside your actual application code (in this case, we dont have the source code)
```
Twitter_API-Pytest
|
|--conftest.py
|--tokens.json
|--test_status_endpoints
    |
    |--test_status_retweet.py
    |--test_status_tweet.py
    |--utils.py
```
`conftest.py` -- configuration for pytest; creation of fixtures, creating custom marks, etc., are coded here.\
`tokens.json` -- tokens needed for API Authentication (OAuth1 is used)\
`test_status_endpoints` -- directory that holds the testcases for different endpoints under `/statuses/<end_points>`.\
Many more directories can be created same manner to hold testcases for multiple endpoints under another URI (example, `test_account_endpoints` to hold the testcases for endpoints under `/account/<end_points>`), that way, the Test project can be extended.\
`test_status_retweet.py` -- holds testcases for making a tweet and destroying the same tweet after done.
`test_status_retweet` -- holds testcases for retweeting our tweet and unretweeting later. Endpoints tested/used are
`utils.py` -- holds utilty methods that can be of common use across testcases.


### Requirement
- Twitter developer account - to use the READ/WRITE/SEARCH tweets (make sure to have the necessary API privilege)
- _python 3.6+_ (I am using python 3.8)
- _pytest_ (unit testing framework we will be using)
- _pytest-html_  (pytest plugin: to make a report of test cases run in HTML format)
- _pytest-ordering_ (pytest plugin: to help in ordering the test cases)
- _requests_oauthlib_ (to help in OAuth1.0 for our API calls)

### Setup
Make sure that the python is installed (not going to cover it here). Use the below command to verify python\
`> python --version`

Now for the setup, Make sure to be in the project directory and execute the below command\
`Twitter_API-Pytest> python -m pip install -r requirement.txt`

If you are using pipenv, use the following command\
`Twitter_API-Pytest> pipenv install -r requirement.txt`

### Usage
The usage is same as executing pytest on a directory with test cases\
(please refer to [pytest documentation](https://docs.pytest.org/en/stable/) for more details and references)

Make sure to be in the project directory & use following Command to trigger pytest\
`Twitter_API-Pytest> pytest --capture=sys -v --html=report.html`

Args of Pytest used :\
`--capture` - captures the console response from the testcases (alternatively we can also use file logging instead of stdout)\
`--html` - generates Test report from the outcome of pytest\
`-v` - Captures more details on the console (std) about the testcases that are executed/skipped/succeeded/failed.

If you using pipenv, use the following command\
`Twitter_API-Pytest> pipenv run pytest --capture=sys --html=report.html`\
or Enter pipenv shell and execute pytest as below
```
Twitter_API-Pytest> pipenv shell
(Twitter_API-Pytest-VL_9mm1P) Twitter_API-Pytest> pytest --capture=sys -v --html=report.html
```

The pytest output will be as below
```
Twitter_API-Pytest>pipenv run pytest --capture=sys -v --html=report.html
================================================= test session starts =================================================
platform win32 -- Python 3.8.5, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- <user_home_dir>\.virtualenvs\twitter_api-pytest-vl_9mm1p\scripts\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.8.5', 'Platform': 'Windows-10-10.0.18362-SP0', 'Packages': {'pytest': '6.1.0', 'py': '1.9.0', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.1.1', 'metadata': '1.10.0', 'ordering': '0.6'}}
rootdir: Twitter_API-Pytest
plugins: html-2.1.1, metadata-1.10.0, ordering-0.6
collected 5 items

test_status_endpoints/test_status_tweet.py::test_make_tweet[We welcome you to MSD family :)] PASSED              [ 20%]
test_status_endpoints/test_status_tweet.py::test_make_tweet[Hello World !!] PASSED                               [ 40%]
test_status_endpoints/test_status_retweet.py::test_make_retweet PASSED                                           [ 60%]
test_status_endpoints/test_status_retweet.py::test_undo_retweet PASSED                                           [ 80%]
test_status_endpoints/test_status_tweet.py::test_delete_tweet PASSED                                             [100%]

----------------------- generated html file: file://Twitter_API-Pytest\report.html ------------------------
================================================== 5 passed in 3.37s ==================================================

```
