
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

searchterm = "#airstrike"
searchcount = 10000

searches = twitter_api.search.tweets(q= searchterm, count = searchcount)
