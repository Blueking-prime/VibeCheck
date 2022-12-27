#!/usr/bin/python3
'''The playlist creation module module'''
from auth import *
from data import *
from algorithms import playlist_tracks, detect_temp_playlists

def create_playlist(name:str, publicity:bool=False, collab:bool=False, desc:str=''):
    '''Creates a new playlist'''
    new_playlist = sp.user_playlist_create(user_id,
                                        name=name,
                                        public=publicity,
                                        collaborative=collab,
                                        description=desc)
    return new_playlist

def add_playlist_songs(playlist: str, track_list: list=playlist_tracks):
    ''' Adds sorted songs to the playlist'''
    sp.user_playlist_add_tracks(user_id, playlist_id=playlist, tracks=track_list)
