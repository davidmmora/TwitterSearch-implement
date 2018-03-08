from TwitterSearch import *

try:
    # create a TwitterUserOrder for user named 'NeinQuarterly'
    tuo = TwitterUserOrder('jekthor') # is equal to TwitterUserOrder(458966079)

    # it's about time to create TwitterSearch object again
    ts = TwitterSearch(
        consumer_key = 'dX1cBXIUbkU3D60wjLGPpQvuz',
        consumer_secret = 'UNCAsjsi2LL5hB8HrURzdd2OWK2n7xKguUFpCmJNsj7rhDAnnp',
        access_token = '99589026-S4bQRrsNmBPXtHlOOeElfbeO6IsBMy4RosMWYLcPH',
        access_token_secret = 'RoUvTsXwce8kkpsOGfFvGLwHg2jTcKaIKyIgwFpC1gNIk'
     )

    # start asking Twitter about the timeline
    for tweet in ts.search_tweets_iterable(tuo):
        print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))

except TwitterSearchException as e: # catch all those ugly errors
    print(e)