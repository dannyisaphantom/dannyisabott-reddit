import praw
import config

def bot_login():
			r = praw.Reddit(username = config.username,
							password = config.password,
							client_id = config.client_id,
							client_secret = config.client_secret,
							ser_agent = "dannyphantom v1")

			return r

def run_bot(r):
			for comment in r.subreddit('test', 'dannyisabott').comments(limit=25):
					if "danny phantom" in comment.body:
							print ("string found!")
							comment.reply("oh hello there")


r = bot_login()
run_bot(r)
# fuck yeah it fucking works! fuck YES!
