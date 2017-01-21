<img src="https://cloud.githubusercontent.com/assets/16360374/21960526/8b68c6ba-daa4-11e6-9f1f-c36faba4d4cb.png" height="100">
------------------------------------------------------------------------------  
#### A Twitch moderator and chat-bot with a few extra built-in features
<p align="right">
    <a href="https://opensource.org/licenses/MIT">
	<img src="https://img.shields.io/apm/l/atomic-monokai-syntax.svg?" height="21" title="License">&nbsp;
    </a>  
    <a href="https://github.com/JonSn0w/TwitchChatBot">
	<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" height="21" title="Open-source">&nbsp;
    </a>
</p>

<p align="center">
	<img src="https://cloud.githubusercontent.com/assets/16360374/21961865/0587b562-daca-11e6-8007-3a8447b7cb02.png" height="300">
</p>

## Description
This is a simple Twitch moderator/chat-bot written in Python, which features automated responses to a collection of commands that provide information, utility, and a little fun to your streams chat.  
By default, the integrated moderator will ban users who attempt to post external links, email addresses, phone numbers, IP addresses, and credit card number. Though, if you'd prefer to instead punish the offending user with a 10 minute timeout from chat, you can do so quite easily by removing ```ban(s, username)``` from the *twitchbot.py* file and uncommenting ```timmeout(s, username)```.

------------------------------------------------------------------------------  

## Setup
  The setup of this chat-bot is fairly simple, though it does require that you have Python 3 installed on your machine. If not, you can download it [**here**](https://www.python.org/downloads/windows/).
  You will also need to download *requests* if it's not already installed. You can install this via the command-line with the command `pip install requests`.

### Configure:
  Next, you will want to open up the *config.py* file and fill out the following fields with your own information.
  * ***NICK*** - Replace the current value with your own username
  * ***PASS*** - You'll need to visit [twitchapps.com/tmi](twitchapps.com/tmi) to get your Twitch.tv OAuth token, which you can *copy+paste* to in the **PASS** section
  * ***CHAN*** - Replace this value with the name of the chat channel you want the bot to be active on. By default, this should probably be your Twitch channel name preceded by a '**#**'.  

### Usage:
  To start the chat-bot program, use the command `python twitchbot.py`  
#### Command-line Arguements
  |   *Arg*           |  *Function*                                          |  
  |:-----------------:|------------------------------------------------------|
  | `-c` / `--config` | Enables configuration via command-line               |
  | `-l` / `--log`    | Enables logging of your chat session to a *.txt* file|

------------------------------------------------------------------------------  

## Commands:

### *Basic*
|   *command*     |  *response*                                    |  
|-----------------|:----------------------------------------------:|
| **Hey/Hello**   | When a greeting is posted in chat this bot will automatically greets the viewer by saying "Welcome to my stream, *\username\*"|
| **@report**     | Allows viewers to report other problematic viewers by running this command followed by the viewer's username |
------------------------------------------------------------------------------  
<br>
### *Channel Stats*
|   *command*   |  *response*                                    |  
|---------------|:----------------------------------------------:|
| **WhatGame**  | Returns the game that is currently streaming   |
|  **Uptime**   | Returns the game that is currently streaming   |
| **ChannelAge**| Returns the age of the channel                 |
| **ViewCount** | Returns the channels current viewer count      |
| **PickViewer**| Returns a random viewer                        |
|   **Time**    | Returns both the amount of time the viewer has followed and subscribed to the channel |

------------------------------------------------------------------------------  
<br>
### *Followers*
|    *command*     |  *response*                                    |  
|------------------|:----------------------------------------------:|
| **FollowerCount**| Returns the number of users following the channel|
| **FollowTime**   | Returns the amount of time the viewer has followed the channel|
| **NewFollow**    | Returns the last user to follow the channel    |
| **PickFollower** | Returns a randomly selected follower           |

------------------------------------------------------------------------------  
<br>
### *Subscribers*
|  *command*   |  *response*                                      |  
|--------------|:------------------------------------------------:|
| **SubCount** | Returns the number of users subscribed to the channel|
| **SubTime**  | Returns the amount of time the viewer has followed the channel|
| **NewSub**   | Returns the last user to subscribe to the channel|
| **PickSub**  | Returns a randomly selected subscriber           |

------------------------------------------------------------------------------  
<br>
### *Just for fun*
|  *command*  |  *response*                                   |  
|-------------|:---------------------------------------------:|
| **8Ball**   | Returns a random answer from the Magic 8-Ball |
| **QOTD**    | Returns a 'Quote of the day'                  |

------------------------------------------------------------------------------  
