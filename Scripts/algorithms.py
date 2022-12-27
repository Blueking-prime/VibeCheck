#!/usr/bin/python3
'''The playlist creation module module'''
from data import *


moods: dict = load_moods()
tracks: dict = load_track_info()
playlist_tracks = []


def create_mood(depth):
    ''' Create a new custom mood'''
    # todo: add mood input fields (maybe change to json edit?)
    # todo: if not json edit, move function input sections to console file
    new_mood = input('What should this new mood be called? ')
    if not depth:
        bpm = input('''What BPM range should this entail? (input the number)
        1 - Slow (20-70 BPM)
        2 - Medium-slow (70-90 BPM)
        3 - Medium (90-110 BPM)
        4 - Medium-fast (110-130 BPM)
        5 - Fast (130-200 BPM)''')

        if bpm == '1':
            bpm = range(20, 70)
        elif bpm == '2':
            bpm = range(20, 70)
        elif bpm == '3':
            bpm = range(20, 70)
        elif bpm == '4':
            bpm = range(20, 70)
        elif bpm == '5':
            bpm = range(20, 70)
        else:
            print('Invalid input')
            return

        details = {'BPM': bpm}
    else:
        key = input('''What mode should the mood represent?
        1 - Minor
        2 - Major
        3 - Doesn't matter''')
        bpm = input('What should the BPM range be? (eg. 50-120)')
        bpm_split = bpm.rpartition('-')
        # todo: add type checking
        details = {'BPM': range(int(bpm_split[0]), int(bpm_split[2])),
                   'mode': int(key) - 1}

    moods.update({new_mood: details})


def select_tracks(mood_name: str, strictness: int):
    '''Selects the tracks to be in the playlist'''
    mood = moods[mood_name]
    track_list = {}
    for key, value in tracks.items():
        confidence = 0
        if value['scale'] == mood['scale'] or mood['scale'] == 2:
            confidence +=1
        if value['BPM'] >= mood['min_BPM'] and value['BPM'] <= mood['max_BPM']:
            confidence += 1
        if value['intensity'] >= mood['min_intensity'] and value['intensity'] <= mood['max_intensity']:
            confidence += 1
        if value['danceability'] >= mood['min_danceability'] and value['intensity'] <= mood['max_danceability']:
            confidence += 1

        if confidence >= strictness:
            print(confidence, value['name'])
            track_list.update({key: value})

    print(len(track_list))
    return track_list


def sort_tracks(tracks):
    # ! incomplete
    pass


def detect_temp_playlists():
    # ! incomplete
    pass
