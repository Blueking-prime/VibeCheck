#!/usr/bin/python3
'''The playlist creation module module'''
from auth import *
from userplaylistdata import *

# TODO: Research and adjust bpm and correlating moods
moods = {'Sad': {'BPM': range(50, 80)}, 'Happy': {}, 'Workout': {}, 'Chill': {}}

# Filter tracks to cut out unnessecary data and append song details
raw_tracks = read_downloads()
tracks = {}
for i in raw_tracks['items']:
    analysis = sp.audio_analysis(i['track']['id'])

    if analysis:
        track_details = {
                        'name': i['track']['name'],
                        'BPM': int(analysis['track']['tempo']),
                        'loudness': analysis['track']['loudness'],
                        'key': analysis['track']['key'],
                        'mode': analysis['track']['key']
                        }
    else:
        track_details = {
                        'name': i['track']['name'],
                        'note': 'No track analysis'
                        }

    tracks.update({i['track']['id']: track_details})

def create_mood():
    ''' Create a new custom mood'''
    # todo: add mood input fields
    new_mood = input('What should this new mood be called? ')
    details = {}
    moods.update({new_mood: details})

def select_tracks(mood):
    # ! incomplete
    pass

def sort_tracks(tracks):
    # ! incomplete
    pass