#!/usr/bin/python3

import json

moods = {
         'Sad': {
                 'min_BPM': 50,
                 'max_BPM': 80,
                 'scale': 0,
                 'min_intensity': 0.000,
                 'max_intensity': 0.300,
                 'min_danceability': 0.000,
                 'max_danceability': 0.500
                },
         'Happy': {
                 'min_BPM': 100,
                 'max_BPM': 160,
                 'scale': 1,
                 'min_intensity': 0.300,
                 'max_intensity': 0.600,
                 'min_danceability': 0.500,
                 'max_danceability': 1.000
                },
         'Workout': {
                 'min_BPM': 160,
                 'max_BPM': 200,
                 'scale': 1,
                 'min_intensity': 0.400,
                 'max_intensity': 1.00,
                 'min_danceability': 0.500,
                 'max_danceability': 1.000
                },
         'Chill': {
                 'min_BPM': 80,
                 'max_BPM': 120,
                 'scale': 2,
                 'min_intensity': 0.000,
                 'max_intensity': 0.100,
                 'min_danceability': 0.000,
                 'max_danceability': 0.200
                }
        }

mood_keys = {
                 'Happy': ['danceability','key', 'loudness', 'BPM', 'intensity', 1],
                 'Sad': ['key', 'BPM', 'loudness', 'intensity', 'danceability', -1],
                 'Workout': ['danceability', 'key', 'loudness', 'intensity', 'BPM', 1],
                 'Chill': ['key', 'BPM', 'danceability', 'loudness', 'intensity', -1]
                }
# with open('../Data/moods_sf.json', 'w', encoding='utf-8') as f:
#     json.dump(mood_keys, f, indent=4)

def open_offline(playlist_name):
    '''Adds a playlist to the list of unuploaded playlists'''
    with open('../Data/local_playlists.json', 'r', encoding='utf-8') as f:
        try:
            playlist_list = json.load(f)
        except json.decoder.JSONDecodeError:
            playlist_list = []
    if not playlist_name:
        return playlist_list

    playlist_list.append(playlist_name)
    with open('../Data/local_playlists.json', 'w', encoding='utf-8') as f:
        json.dump(playlist_list, f, indent=4)

open_offline('tanger')