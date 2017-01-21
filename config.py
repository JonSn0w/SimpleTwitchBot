# config.py
import re

HOST = "irc.twitch.tv"                        # the Twitch IRC server
PORT = 6667                                   # always use port 6667!
NICK = "user_name"                            # your Twitch username, lowercase
PASS = "oauth:..."                            # your Twitch OAuth token
CHAN = "#channel_name"                        # the channel you want to join
RATE = 1.5                                    # messages per second

LOG = False          # set to 'True' if you would like to keep a log of the chat

# ****
#  The first element is an example of how to filter unwanted words or phrases,
#  you may also comment out any of the following content that you would like to
#  allow in chat.
#     NOTE: When adding or removing filters, make sure to include a ',' after
#           each violation except for the last one.
# ****
VIOLATIONS = [
    re.compile(r'Place an unwanted word/phrase here', re.IGNORECASE),
    # match phone numbers
    r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',
    # match links
    re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.IGNORECASE),
    # match email addresses
    re.compile(r"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", re.IGNORECASE),
    # match IP addresses
    r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
    # match credit card numbers
    re.compile(r'((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])', re.IGNORECASE),
]
