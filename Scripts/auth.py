#!/usr/bin/python3
import socket
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import cred

# User permission scopes, append as necessary
scope = "user-library-read,playlist-modify-private,playlist-modify-public"

def network_test(test_host="8.8.8.8", port=53, timeout=3):
    global network_status, work_status, sp, user_id
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((test_host, port))
        print('Connected to Network')
        # Creates spotify client
        sp = Spotify(auth_manager=SpotifyOAuth(client_id=cred.a,
                                                    client_secret=cred.b,
                                                    redirect_uri=cred.c,
                                                    scope=scope))
        # Obtains user ID
        network_status = True
        work_status = True
        user = sp.me()
        if user:
            user_id = user['id']
        else:
            print('Unable to identify User')
            work_status = 'n'

    except socket.error as ex:
        print('Currently unable to connect to Network')
        network_status = False
        while True:
            work_status = input('Do you want to keep working offline [Y/N]? ').lower()
            if work_status != 'y' and work_status != 'n' and work_status != '':
                print('Please choose Y or N')
                continue
            break
        pass

network_test()