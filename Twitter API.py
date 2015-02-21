
import twitter
CONSUMER_KEY = 'qOZP6eyiLMPyoNiZI9AA14lmQ'
CONSUMER_SECRET ='xP6Yazxt0hOriHcqYMoeQwUPkmtLrprNwjGwCEvvsfEb44pJPQ'
OAUTH_TOKEN = '15772978-OWFYt8nmrD4eFrggQck1RwPdocRl33Z4psojUlDui'
OAUTH_TOKEN_SECRET = 'mrYabA6pIdXF62trTKjGWm4J7uxkLRidfVpzDzpWB30FE'

                           
auth = twitter.oauth.OAuth(OAUTH_TOKEN,
                          OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY,
                           CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

searchterm = "#ObamaLovesAmerica"
searchcount = 10

searches = twitter_api.search.tweets(q= searchterm, count = searchcount)
tweetTextArray = [s['text'] for s in searches['statuses']]

from SentimentApi import analyze_text

for tweet in tweetTextArray:
	rating = analyze_text(tweet)
	print(tweet.strip(),)
	if (rating > 0):
		print(" -- POSITIVE")
	elif (rating < 0):
		print(" -- NEGATIVE")
	else:
		print(" -- NEUTRAL")