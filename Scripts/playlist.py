#!/usr/bin/python3
'''The playlist creation module module'''
from auth import *
from data import *


def create_playlist(name:str, publicity:bool=False, collab:bool=False, desc:str=''):
    '''Creates a new playlist'''
    new_playlist = sp.user_playlist_create(user_id,
                                        name=name,
                                        public=publicity,
                                        collaborative=collab,
                                        description=desc)
    return new_playlist

def add_playlist_songs(playlist_id:str, tracks:dict):
    ''' Adds sorted songs to the playlist'''
    track_list = []
    # Extracts ids from the track dict
    for i in tracks:
        track_list.append(i)
    sp.user_playlist_add_tracks(user_id, playlist_id=playlist_id, tracks=track_list)

def get_playlist_id(playlist_name:str|None):
    '''Gets the id of the playlist'''
    playlist_id = None
    playlists = load_users_playlists()
    if playlists:
        playlists = playlists['items']
    else:
        return None

    if playlist_name:
        for i in playlists:
            if i['name'] == playlist_name:
                playlist_id = i['id']
                break
        return playlist_id
    else:
        playlist_list = []
        for i in playlists:
            playlist_list.append((i['id'], i['name']))
        return playlist_list
