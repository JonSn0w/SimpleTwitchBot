# bot.py
import re
import cfg
from time import sleep
import urllib
import requests
import socket

# Put your channel name here
CHANNEL = "hello_murdoc"

# network functions
s = socket.socket()
s.connect((cfg.HOST, cfg.PORT))
s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

def respond(msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    msg -- the message to be sent
    """
    s.send("PRIVMSG #hello_murdoc :" + msg + "\r\n")
    print("BOT: " + msg + "\r\n")

def chat(sock, msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    sock -- the socket over which to send the message
    msg  -- the message to be sent
    """
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def ban(sock, user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    sock -- the socket over which to send the ban command
    user -- the user to be banned
    """
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    sock -- the socket over which to send the timeout command
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    chat(sock, ".timeout {}".format(user, secs))

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        message = CHAT_MSG.sub("", response)
        print(username + ": " + message)
        if re.match("Hey", message, re.IGNORECASE) or re.match("Hello", message, re.IGNORECASE):
            # Responds to viewer greetings
            respond("Welcome to my stream, " + username)

        # Channel Stats
        elif re.match("ChannelAge", message, re.IGNORECASE):
            # Returns the age of the channel
            response = requests.get('http://api.rtainc.co/twitch/channels/'+ CHANNEL + '?format=%5B0%5D%27s+account+has+existed+for+%5B1%5D')
            respond(response.content)
        elif re.match("WhatGame", message, re.IGNORECASE):
            # Returns the game being played
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/status?format=%5B0%5D+is+currently+playing+%5B1%5D')
            respond(response.content)
        elif re.match("Uptime", message, re.IGNORECASE):
            # Returns the length of the current stream
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/uptime?format=%5B0%5D%27s+stream+has+been+up+for+%5B1%5D&units=2')
            respond(response.content)
        elif re.match("ViewCount", message, re.IGNORECASE):
            # Returns the game being played
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/status?format=%5B0%5D+currently+has+%5B2%5D+viewers')
            respond(response.content)
        elif re.match("PickViewer", message, re.IGNORECASE):
            # Returns a random viewer
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/viewers/random?format=I+choose...+%5B0%5D')
            respond(response.content)

        # Follower Stats
        elif re.match("FollowerCount", message, re.IGNORECASE):
            # Returns the number of followers
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/count?format=%5B0%5D+has+%5B1%5D+followers')
            respond(response.content)
        elif re.match("FollowTime", message, re.IGNORECASE):
            # Returns how long the viewer has followed the channel
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/'+username+'?format=%5B1%5D+has+been+following+%5B0%5D+for+%5B2%5Dunit=3')
            respond(response.content)
        elif re.match("PickFollower", message, re.IGNORECASE):
            # Returns a random subscriber
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/random?format=I+choose...+%5B0%5D&token=TOKEN')
            respond(response.content)
        elif re.match("NewFollow", message, re.IGNORECASE):
            # Returns the channels newest follower
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers?format=%5B0%5D%27s+last+%5B1%5D+followers+are:+%5B2%5D&count=1')
            respond(response.content)

        # Subscriber Stats
        elif re.match("SubCount", message, re.IGNORECASE):
            # Returns the number of subscribers
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/count?format=%5B0%5D+has+%5B1%5D+subs&token=TOKEN')
            respond(response.content)
        elif re.match("SubTime", message, re.IGNORECASE):
            # Returns how long the viewer has followed the channel
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/'+username+'?format=%5B1%5D+has+been+subbed+to+%5B0%5D+for+%5B2%5D&token=TOKEN')
            respond(response.content)
        elif re.match("NewSub", message, re.IGNORECASE):
            # Returns the channels newest subscriber
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs?format=%5B0%5D%27s+last+%5B1%5D+subs+are:+%5B2%5D&count=1')
            respond(response.content)
        elif re.match("PickSub", message, re.IGNORECASE):
            # Returns a random subscriber
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/random?format=I+choose...+%5B0%5D&token=TOKEN')
            respond(response.content)

        elif re.match("Time", message, re.IGNORECASE):
            # Returns how long the viewer has followed and how long the viewer has subscribed to the channel
            follower = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/'+username+'?format=%5B1%5D+has+been+following+%5B0%5D+for+%5B2%5Dunit=3')
            sub = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/'+username+'?format=%5B1%5D+has+been+subbed+to+%5B0%5D+for+%5B2%5D&token=TOKEN')
            respond(follower.content +' and '+ sub.content)

        # Just for Fun
        elif re.match("QOTD", message, re.IGNORECASE):
            # Returns the quote of the day
            response = requests.get('http://api.rtainc.co/twitch/brainyquote?format=Your+quote+of+the+day+is:+%22%5B0%5D%22&type=br')
            respond(response.content)
        elif re.match("8Ball", message, re.IGNORECASE):
            # Magic 8-Ball answers
            response = requests.get('http://api.rtainc.co/twitch/8ball?format=The+Magic+8-Ball+says...+%5B0%5D')
            respond(response.content)

        # Chat Violations
        for pattern in cfg.VIOLATIONS:
            if re.match(pattern, message):
                # ban(s, username)
                print('match')
                break
    sleep(1/cfg.RATE)
