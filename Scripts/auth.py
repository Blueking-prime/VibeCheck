#!/usr/bin/python3
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

# User permission scopes, append as necessary
scope = "user-library-read,playlist-modify-private,playlist-modify-public"

# Creates spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id,
                                               client_secret=cred.client_secret,
                                               redirect_uri=cred.redirect_url,
                                               scope=scope))

# Obtains user ID
# todo: add method for obtaining user id (prolly use 'me' or something)
user_id = ''
