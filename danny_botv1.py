# updated code, 'r' has been changed to 'reddit' to be more descriptive
# some major updates throughout

import praw
# removed import config as we can host multiple bot info in the praw.ini file under bot names
# bot is nowhere near done; this is just an update to the code
import time

def authenticate():
	print("authenticating.")
	reddit = praw.Reddit('dannyphantombot', user_agent = "dannyphantom v0.1")

	print("authenticated as {}".format(reddit.user.me()))
	# returns the currently authorized reddit username

	return reddit

def main():
	reddit = authenticate()
	while True:
		run_bot(reddit)

def run_bot(reddit):
	print ("grabbing 25 comments")
	for comment in reddit.subreddit('test').comments(limit=25):
					if "danny phantom" in comment.body:
							print ("string with \"danny phantom\" found in comment" + comment.id)
							comment.reply("oh hello there")
							print ("replied to comment" + comment.id)

	print ("sleeping 15s")
	#sleeps for 15 seconds
	time.sleep(15)

if __name__ == '__main__':
	main()
# to use in a different program: from [RedditBot] import run_bot which is seen above -> from RedditBot import run_bot

