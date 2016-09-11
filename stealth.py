# StealthNietzsche - A Twitter bot spell-checking the name of everyone's favorite philosopher

import tweepy

import settings

# super-secret keys for talking to twitter !!!!ADD SETTINGS TO GITIGNORE!!!!
CONSUMER_KEY = settings.Consumer_Key
CONSUMER_SECRET = settings.Consumer_Key_Secret
ACCESS_KEY = settings.Access_Token 
ACCESS_SECRET = settings.Access_Token_Secret

# Authorization for the Tweepy OAuth handler
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# set variable to the Tweepy API with the auth credentials
api = tweepy.API(auth)


# Create a list of false spellings of Nietzsche to  be checked against
# note the correct name and create the chide to use on people using the misspelled name
incorrect_names  = ["Nietche", "Neitzsche", "Nietzhce", "Niezthe", "Nietache"]
CORRECT_NAME = "Nietzsche"
chide = "Not to be a jerk, but I think you meant 'Nietzsche'"


#tweets = [api.search(q=name) for name in incorrect_names]
public_tweets = [api.search(q=name) for name in incorrect_names]
# for result in public_tweets:
# 	for tweet in result:
# 		print(tweet.text)

for result in public_tweets:
	for tweet in result:
		if not CORRECT_NAME in tweet.text:
			foo = tweet.author._json['screen_name']
			#print(foo)
			#bar = tweet.id
			#print(bar)
			tweet_range = api.user_timeline(count=2, page=12)
			print(tweet_range)
			
		message = "@{} {}".format(foo, chide)
		print (message)
		to_tweet = message
		really_tweet = (message)
		s = api.update_status(message, s.id)
 		


"""
NOTES:
 -
"""