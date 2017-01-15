# cfg.py
import re

HOST = "irc.twitch.tv"                        # the Twitch IRC server
PORT = 6667                                   # always use port 6667!
NICK = "hello_murdoc"                         # your Twitch username, lowercase
PASS = "oauth:..."                            # your Twitch OAuth token
CHAN = "#hello_murdoc"                        # the channel you want to join
RATE = 1.5                                    # messages per second

VIOLATIONS = [
    r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})',   # match phone numbers
    re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.IGNORECASE),   # match links
    re.compile(r"([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", re.IGNORECASE),  # match email addresses
    r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', # match IP addresses
    re.compile(r'((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])', re.IGNORECASE),  # match credit card numbers
]
