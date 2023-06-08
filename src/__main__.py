import requests
import json
import time
from math import floor
from twitter.account import Account
from config import (
    TWITTER_EMAIL,
    TWITTER_USERNAME,
    TWITTER_PASSWORD,
    LASTFM_USERNAME,
    LASTFM_API_KEY,
    DESCRIPTION,
    CHECK_INTERVAL,
)


def get_music():
    # I hate this
    tracks = requests.get(
        f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={LASTFM_USERNAME}&api_key={LASTFM_API_KEY}&limit=1&format=json"
    )
    tracks = json.loads(tracks.text)["recenttracks"]["track"][0]
    return tracks["name"], tracks["artist"]["#text"]


def set_description(title, artist):
    # 160 is the max length of a twitter bio
    max_length = floor((160 - len(DESCRIPTION)) / 2)

    if len(title) + len(artist) > max_length * 2:
        if len(title) > max_length:
            title = title[: max_length - 3] + "..."
        if len(artist) > max_length:
            artist = artist[: max_length - 3] + "..."

    account.update_profile_info(description=DESCRIPTION % (title, artist))


if __name__ == "__main__":
    account = Account(
        TWITTER_EMAIL, TWITTER_USERNAME, TWITTER_PASSWORD, debug=2, save=True
    )
    last_song = None

    while True:
        title, artist = get_music()

        if last_song != title and title and artist:
            set_description(title, artist)
            last_song = title

        time.sleep(CHECK_INTERVAL)
