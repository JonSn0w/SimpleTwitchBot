# twitchbot.py

import re
import sys
import config
import socket
import requests
from time import sleep
import datetime
from datetime import date

log = config.LOG
cfg = True
if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg == "--config" or sys.argv[1] == "-c":
            USERNAME = raw_input("Username: ")
            CHANNEL = raw_input("Channel: ")
            PASSS = raw_input("OAuth: ")
            cfg = False
        elif arg == "--log" or arg == "-l":
            log = True
        elif arg != "twitchbot.py":
            print("***ERROR: The following command-line arguement, \'"+sys.argv[1]+"\', is not valid modifier.***")
            sys.exit()
if cfg:
    # Put your channel name here
    USERNAME = config.NICK
    CHANNEL = config.CHAN[1:]
    PASS = config.PASS

# network functions
s = socket.socket()
s.connect((config.HOST, config.PORT))
s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(USERNAME).encode("utf-8"))
s.send("JOIN {}\r\n".format('#'+CHANNEL).encode("utf-8"))
CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

def chat(msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    msg -- the message to be sent
    """
    s.send("PRIVMSG #" + CHANNEL + " :" + msg + "\r\n")
    if log:
        log("BOT: " + msg + "\r\n")
    print("BOT: " + msg + "\r\n")

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

def initLog():
    today = date.today()
    return "log/log_" + str(today.month) + '-' + str(today.day) + '-' + str(today.year) + ".txt"

def log(msg):
    logger=open(logFile,'a+')
    logger.write(msg)

def cleanLog():
    filtered = []
    oldLog = open(logFile, 'r+')
    contents = oldLog.readlines()
    for line in contents:
        if 'tmi.twitch.tv' not in line and line[0] != ':':
            filtered.append(line)
    newLog = open(logFile, 'w+')
    newLog.writelines(filtered);

# class Report:
    # """
    # A custom data type for report submissions
    # Keyword arguments:
    # self   -- the Report itself
    # report -- the viewer being reported
    # user   -- the user that submitted the report
    # """
    # def __init__(self, report, user):
    #     self.report = report
    #     self.user = user

def report(user, report):
    # """
    # Allows users to report probematic viewers using the '@report' command and stores the reports to be reviewed later by the streamer.
    # Keyword arguments:
    # user   -- the user submitting the report
    # report -- the viewer being reported
    # """"
    f = open('reportLog.txt', 'a+')
    f.write(user + " (reported by " + user + ")\n")
    print("***Report logged***")

logFile= ""
if log:
    logFile = initLog()

count = 0
while sys.stdin.isatty():
    if count == 2 and log:
        cleanLog()
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        username = re.search(r"\w+", response).group(0)
        message = CHAT_MSG.sub("", response)
        if log:
            log(str(username) + ": " + str(message))
            print(username + ": " + message)
        if re.match("Hey", message, re.IGNORECASE) or re.match("Hello", message, re.IGNORECASE):
            # chats to viewer greetings
            chat("Welcome to my stream, " + str(username) + "!")
        if re.match("@report", message, re.IGNORECASE):
            report(username, message[8:])

        # Viewer reports

            # Channel Stats
        elif re.match("ChannelAge", message, re.IGNORECASE):
            # Returns the age of the channel
            response = requests.get('http://api.rtainc.co/twitch/channels/'+ CHANNEL + '?format=%5B0%5D%27s+account+has+existed+for+%5B1%5D')
            chat(response.content)
        elif re.match("WhatGame", message, re.IGNORECASE):
            # Returns the game being played
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/status?format=%5B0%5D+is+currently+playing+%5B1%5D')
            chat(response.content)
        elif re.match("Uptime", message, re.IGNORECASE):
            # Returns the length of the current stream
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/uptime?format=%5B0%5D%27s+stream+has+been+up+for+%5B1%5D&units=2')
            chat(response.content)
        elif re.match("ViewCount", message, re.IGNORECASE):
            # Returns the channels current viewer count
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/status?format=%5B0%5D+currently+has+%5B2%5D+viewers')
            chat(response.content)
        elif re.match("PickViewer", message, re.IGNORECASE):
            # Returns a random viewer
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/viewers/random?format=I+choose...+%5B0%5D')
            chat(response.content)

            # Follower Stats
        elif re.match("FollowerCount", message, re.IGNORECASE):
            # Returns the number of followers
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/count?format=%5B0%5D+has+%5B1%5D+followers')
            chat(response.content)
        elif re.match("FollowTime", message, re.IGNORECASE):
            # Returns how long the viewer has followed the channel
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/'+username+'?format=%5B1%5D+has+been+following+%5B0%5D+for+%5B2%5D')
            chat(response.content)
        elif re.match("PickFollower", message, re.IGNORECASE):
            # Returns a random subscriber
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/random?format=I+choose...+%5B0%5D&token=TOKEN')
            chat(response.content)
        elif re.match("NewFollow", message, re.IGNORECASE):
            # Returns the channels newest follower
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers?format=%5B0%5D%27s+last+%5B1%5D+followers+are:+%5B2%5D&count=1')
            chat(response.content)

            # Subscriber Stats
        elif re.match("SubCount", message, re.IGNORECASE):
            # Returns the number of subscribers
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/count?format=%5B0%5D+has+%5B1%5D+subs&token=TOKEN')
            chat(response.content)
        elif re.match("SubTime", message, re.IGNORECASE):
            # Returns how long the viewer has followed the channel
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/'+username+'?format=%5B1%5D+has+been+subbed+to+%5B0%5D+for+%5B2%5D&token=TOKEN')
            chat(response.content)
        elif re.match("NewSub", message, re.IGNORECASE):
            # Returns the channels newest subscriber
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs?format=%5B0%5D%27s+last+%5B1%5D+subs+are:+%5B2%5D&count=1')
            chat(response.content)
        elif re.match("PickSub", message, re.IGNORECASE):
            # Returns a random subscriber
            response = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/random?format=I+choose...+%5B0%5D&token=TOKEN')
            chat(response.content)

        elif re.match("Time", message, re.IGNORECASE):
            # Returns how long the viewer has followed and how long the viewer has subscribed to the channel
            follower = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/followers/'+username+'?format=%5B1%5D+has+been+following+%5B0%5D+for+%5B2%5Dunit=3')
            sub = requests.get('http://api.rtainc.co/twitch/channels/'+CHANNEL+'/subs/'+username+'?format=%5B1%5D+has+been+subbed+to+%5B0%5D+for+%5B2%5D&token=TOKEN')
            chat(follower.content +' and '+ sub.content)

            # Just for Fun
        elif re.match("QOTD", message, re.IGNORECASE):
            # Returns the quote of the day
            response = requests.get('http://api.rtainc.co/twitch/brainyquote?format=Your+quote+of+the+day+is:+%22%5B0%5D%22&type=br')
            chat(response.content)
        elif re.match("8Ball", message, re.IGNORECASE):
            # Magic 8-Ball answers
            response = requests.get('http://api.rtainc.co/twitch/8ball?format=The+Magic+8-Ball+says...+%5B0%5D')
            chat(response.content)

        # Chat Violations
        for pattern in config.VIOLATIONS:
            if re.match(pattern, message):
                ban(s, username)
                # timeout(s, username)  # Give user (10 min) timeout from chat
                break
        count = count + 1
        sleep(1/config.RATE)

# if not sys.stdin.isatty():
#     print "not sys.stdin.isatty"
#     input = raw_input("")
#     if input == "exit":
#         print ("Closing...")
#         sys.exit()
#     else:
#         msvcrt.getch()
