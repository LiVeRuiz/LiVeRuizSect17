import tweepy
import time

auth = tweepy.OAuthHandler("bYeoFLs542DvxkWEGFLvjJGNb", "8i53eZf3KqZW73W3STcJ0NUSMdOVcqUJFrrqNwEsWy0Jt94BPQ")
auth.set_access_token("53129805-XhMn9ikf4OV7VCUQGgSy3FQONFdoqHNdR6jcaIRsl", "Xi8PgkzvFYt397FbHC2iXXUSUs8ZZw0KOQ1tlSiyGDi66")

api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()
	except tweepy.RateLimitError:
		time.sleep(300) #pause in miliseconds


search_string = 'veronica ruiz'
numberOfTweets = 10

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason)
	except StopOteration:
		break