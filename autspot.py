import requests
import Leconfigs
CLIENT_ID = 'yourclientid'
CLIENT_SECRET = 'yourclientsecret'

CLIENT_ID=Leconfigs.clientID
CLIENT_SECRET=Leconfigs.clientSecret

AUTH_URL = 'https://accounts.spotify.com/api/token'

print(CLIENT_ID)
print(CLIENT_SECRET)

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']