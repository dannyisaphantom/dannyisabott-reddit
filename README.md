# dannyisabott
- a reddit reply bot
- documenting what i'm doing along the way as a way to teach myself and others if anyone ever comes across my profile (not likely)
Tools: [Python 3.9.1](https://www.python.org/downloads/), [Reddit](reddit.com) & [Praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html)

- ongoing updates to the bot will follow the danny_botv1.1, 1.2, 1.3, etc format.

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
using Atom
create a config.py so that it's formatted like below
```
username="dannyisabott"
password="x"
client_id="y"
client_secret="z"
```
then, in cmd line of your files directory enter:
> move config.py praw.ini

after the file is converted to praw.ini open it in your text editor where you'll make some changes
most notably you'll enter your credentials within brackets; within this praw.ini file you can now make multiple profiles for different bots and have them reference different "profiles"; see config.py to praw.ini to get a better understanding of what that means
```
[dannyphantombot]
username: dannyisabott
password: 123xyz
client_id: xyz
client_secret: xyz
```

then, in reddit_bot1.py i define my values like this:
```
import praw
praw.Reddit('dannyphantombot', user_agent = "dannyphantom v0.1")
```


