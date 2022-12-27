#!/usr/bin/python3
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import cred

# User permission scopes, append as necessary
scope = "user-library-read,playlist-modify-private,playlist-modify-public"

# Creates spotify client
sp = Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id,
                                               client_secret=cred.client_secret,
                                               redirect_uri=cred.redirect_url,
                                               scope=scope))

# Obtains user ID
user = sp.me()
if user:
    user_id = user['id']
else:
    print('Unable to identify User')
