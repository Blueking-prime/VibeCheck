#!/usr/bin/python3
'''The playlist creation module module'''
from auth import *
from userplaylistdata import *

def show_saved():
    '''Prints out track info saved locally'''
    results: dict = read_downloads()
    for i in results['items']:
        print(i['track']['name'])

def create_playlist(name, publicity=False, collab=False, desc=''):
    '''Creates a new playlist'''
    new_playlist = sp.user_playlist_create(user_id,
                                        name=name,
                                        public=publicity,
                                        collaborative=collab,
                                        description=desc)
    return new_playlist

def add_playlist_songs(playlist, track_list):
    ''' Adds sorted songs to the playlist'''
    # ! incomplete
    sp.user_playlist_add_tracks(user_id, playlist_id=playlist, tracks=track_list)
