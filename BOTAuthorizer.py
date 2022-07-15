#Pequeño Script utilizado para autorizar perfiles con twitter y así poder postear desde esas cuentas
import tweepy

CONSUMER_KEY = "INSERTAR CONSUMER KEY"
CONSUMER_SECRET = "INSERTAR CONSUMER SECRET"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback = 'oob')
auth.secure = True
auth_url = auth.get_authorization_url()

print ('Please authorize: ' + auth_url)

verifier = input('PIN: ').strip()

auth.get_access_token(verifier)

print ("ACCESS_KEY = " + auth.access_token)
print ("ACCESS_SECRET = " +  auth.access_token_secret)