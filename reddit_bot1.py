import praw
import config

    def bot_login():
       r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "dannyphantom v0.1")

       return r
    def run_bot(r):
        for comment in r.subreddit('test').comments(limit=25):
            if "danny phantom" in comment.body
                print"string found!"

  r = bot_login()
