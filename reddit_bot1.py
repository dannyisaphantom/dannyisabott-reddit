# in my text editor, this is a seperate tab named "reddit_bot1.py

import praw
import config
# it's important to define the parameters within the config
praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "something v0.1") 
            # user_agent is how you wish to label your versions/bots
