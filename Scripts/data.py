#!/usr/bin/python3
'''Data handling and storage module'''
import json
from auth import *


# Downloads section
def update(playlist_id:str|None=None, playlist_name:str|None=None):
    '''Updates local storage'''
    download_tracks(playlist_id, playlist_name)
    download_track_info(load_downloads(playlist_name))

def download_tracks(playlist_id: str|None = None, playlist_name: str|None = None):
    '''Downloads users track info and saves it locally'''
    if not playlist_id or not playlist_name:
        tracks = sp.current_user_saved_tracks(limit=1000)
        with open('../Data/track_dump.json', 'w', encoding='utf-8') as f:
            json.dump(tracks, f)
    else:
        # Downloads playlist track info and saves it locally
        tracks = sp.user_playlist(user_id, playlist_id=playlist_id)
        with open(f'../Data/{playlist_name}.json', 'w', encoding='utf-8') as f:
            json.dump(tracks, f)

def download_track_info(raw_tracks: dict):
    '''Downloads all track details'''
    # Filter tracks to cut out unnessecary data and append song details
    tracks = {}
    for i in raw_tracks['items']:
        # Gets tracks possible genres (May remove)
        # genres = []
        # artists = sp.artist(i['track']['artists'])
        # artist_ids = []
        # for j in artists:
        #     artist_ids.append(j['id'])
        # artist_info = sp.artists(artist_ids)
        # for k in artist_info:
        #     genres.append(k['genres'])

        # Obtains other track details
        analysis = sp.audio_features(i['track']['id'])

        # mode, bpm, danceablity, intensity and scale for song selection
        # BPM, key, loudness, intensity and danceablility for sorting
        if analysis:
            analysis = analysis[0] # This is cause audio_features() returns a list
            track_details = {
                            'name': i['track']['name'],
                            'BPM': int(analysis['tempo']),
                            'loudness': float(analysis['loudness']),
                            'key': int(analysis['key']),
                            'scale': int(analysis['mode']),
                            'intensity': float(analysis['energy']),
                            'danceability': float(analysis['danceability'])
                            }
        else:
            print(f"Failed to analyze track: {i['track']['name']} - id: {i['track']['id']}")
            track_details = {
                            'name': i['track']['name'],
                            'note': 'No track analysis'
                            }

        tracks.update({i['track']['id']: track_details})

    with open('../Data/track_info.json', 'w', encoding='utf-8') as f:
        json.dump(tracks, f, indent=4)


# Load from local storage section
def load_downloads(playlist_name: str | None):
    '''Loads data from stored file'''
    if not playlist_name:
        with open('../Data/track_dump.json', 'r', encoding='utf-8') as f:
            saved: dict = json.load(f)
        return saved
    else:
        with open(f'../Data/{playlist_name}.json', 'r', encoding='utf-8') as f:
            saved: dict = json.load(f)
        return saved

def load_moods():
    with open('../Data/moods.json', 'r', encoding='utf-8') as f:
        moods: dict = json.load(f)
    return moods

def load_mood_sf():
    with open('../Data/moods_sf.json', 'r', encoding='utf-8') as f:
        sf: dict = json.load(f)
    return sf

def load_track_info():
    with open('../Data/track_info.json', 'r', encoding='utf-8') as f:
        track_info: dict = json.load(f)
    return track_info

def show_saved():
    '''Prints out tracks saved locally'''
    results: dict = load_downloads(None)
    for i in results['items']:
        print(i['track']['name'])