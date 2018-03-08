from datetime import *
from TwitterSearch import *
try:
    tso = TwitterSearchOrder() #Creando un objeto TwitterSearchOrder
    # tso.set_keywords(['AMLO' ,'PRESIDENTE', '2018', 'since:2018-03-01','until:2018-03-01']) # definiendo palabras a buscar en el tweet
    tso.set_keywords(['AMLO' ,'PRESIDENTE', '2018']) # definiendo palabras a buscar en el tweet
    tso.set_language('es') # idioma de los tweets
    tso.set_include_entities(False) # nodo de entidad
    tso.set_since(date(2018, 2,28))

    # creando objeto con los tokens secretos de la app creada en twitter
    ts = TwitterSearch(
        consumer_key = 'dX1cBXIUbkU3D60wjLGPpQvuz',
        consumer_secret = 'UNCAsjsi2LL5hB8HrURzdd2OWK2n7xKguUFpCmJNsj7rhDAnnp',
        access_token = '99589026-S4bQRrsNmBPXtHlOOeElfbeO6IsBMy4RosMWYLcPH',
        access_token_secret = 'RoUvTsXwce8kkpsOGfFvGLwHg2jTcKaIKyIgwFpC1gNIk'
     )

     # inicio de funcion para busqueda del objeto ya creado
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s Tweteado: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # Control de errores
    print(e)