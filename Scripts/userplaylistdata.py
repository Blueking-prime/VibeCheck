#!/usr/bin/python3
'''Data handling and storage module'''
import json
from auth import *

def download_saved_tracks():
    '''Downloads users track info and saves it locally'''
    tracks = sp.current_user_saved_tracks()
    with open('../Data/track_info.json', 'w', encoding='utf-8') as f:
        json.dump(tracks, f)

def download_playlist(playlist_id, playlist_name):
    '''Downloads playlist track info and saves it locally'''
    tracks = sp.user_playlist(user_id, playlist_id=playlist_id)
    with open(f'../Data/{playlist_name}.json', 'w', encoding='utf-8') as f:
        json.dump(tracks, f)

def read_downloads(playlist_name=None):
    '''Loads data from stored file'''
    if not playlist_name:
        with open('../Data/track_info.json', 'r', encoding='utf-8') as f:
            saved = json.load(f)
        return saved
    else:
        with open(f'../Data/{playlist_name}.json', 'r', encoding='utf-8') as f:
            saved = json.load(f)
        return saved

