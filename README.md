# Twitter-LastFM
Show currently playing track on your profile

## Warning
I cannot guarantee that your account will not be banned for using this script, use at your own risk.
You also need to disable 2fa as of currently as the Twitter api package this script uses relies on web scraping.

## Usage
create a file named `config.py` in `/src` and add the following lines:
```python
DESCRIPTION = "Your Bio and %s by %s for the currently playing song"
CHECK_INTERVAL = 10  # in seconds

TWITTER_EMAIL = "example@provider.com"
TWITTER_USERNAME = "example"
TWITTER_PASSWORD = "password"

LASTFM_USERNAME = "example"
LASTFM_API_KEY = "123456789abcdefghijklmnopqrstuvw"
```
