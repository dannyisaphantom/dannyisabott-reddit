# dannyisabott
- a reddit reply bot
- documenting what i'm doing along the way as a way to teach myself and others if anyone ever comes across my profile (not likely)
Tools: [Python 3.9.1](https://www.python.org/downloads/), [Reddit](reddit.com) & [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)

## reddit api access
- create basic reddit account and follow this link: https://www.reddit.com/prefs/apps/
- for the redirect uri i used: http://localhost: ** keep note of your client_id at the top and secret which is a longer string **

### from cmd line
- enter:
> pip install praw:
- wait for install to complete and then follow up with
> pip install --upgrade praw 

now you have the latest update of praw installed

## code editor 

i am now using pyCharm; but i am going to test this within Atom as well; i have config.py that defines my login details
```
username="dannyisabott"
password="x"
client_id="y"
client_secret="z"
```
then, in reddit_bot1.py i define my values like this:
```
import praw
import config
praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "dannyphantom v0.1")
```
### cmd line testing
i want to focus on where i put my file, so within my own cmd i say:
```
cd ~/Desktop/redditbot
it will respond C:\users\jake\desktop\redditbot>reddit_bot1.py (which is my .py file)
and, it will then go to C:\users\jake\redditbot (again) awesome.
```
keep in mind, that is my directory so be sure to change to where you save your .py file and also keep in mind nothing happened with the above code.
this is all farily obvious to most python coders but this is primarily for me to keep tabs on so i can learn as i go

i edited the reddit_bot1.py code to include:
```
import praw
import config

  def bot_login():
      praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "dannyphantom v0.1")
```
and it works! fuck yes! 
issues regarding spacing and tab became apparent which i didnt expect but when executed on cmd it works\
this was within Sublime Text; testing in Atom had only spacial errors which were easily fixed as well. 
