from twython import Twython
import sys

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

message = sys.argv[1]
twitter.update_status(status=message)
print("Tweeted: " + message)
