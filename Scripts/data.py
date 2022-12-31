#!/usr/bin/python3
'''Data handling and storage module'''
from os import remove
import json
import auth

# Downloads section
def update(playlist_id=None, playlist_name=None):
    '''Updates local storage'''
    download_tracks(playlist_id, playlist_name)
    download_track_info(load_downloads(playlist_name))

def download_tracks(playlist_id: str|None = None, playlist_name: str|None = None):
    '''Downloads users track info and saves it locally'''
    if not playlist_id or not playlist_name:
        tracks = auth.sp.current_user_saved_tracks(limit=50)
        if tracks:
            while tracks['next']:
                page = auth.sp.current_user_saved_tracks(limit=50, offset=50)
                if page:
                    tracks['items'] += page['items']
                    tracks['next'], tracks['previous'] = page['next'], page['previous']

            with open('../Data/track_dump.json', 'w', encoding='utf-8') as f:
                json.dump(tracks, f)
        else:
            print('Unable to retreive saved playlists')
    else:
        # Downloads playlist track info and saves it locally
        tracks = auth.sp.playlist_items(playlist_id, limit=50)
        if tracks:
            while tracks['next']:
                page = auth.sp.playlist_items(playlist_id, offset=50)
                if page:
                    tracks['items'] += page['items']
                    tracks['next'], tracks['previous'] = page['next'], page['previous']

            with open(f'../Data/Spotify_Playlists/{playlist_name}.json', 'w', encoding='utf-8') as f:
                json.dump(tracks, f)
        else:
            print('Unable to retreive playlist')

def download_track_info(raw_tracks: dict):
    '''Downloads all track details'''
    # Filter tracks to cut out unnessecary data and append song details
    tracks = {}
    for i in raw_tracks['items']:
        # Gets tracks possible genres (May remove)
        # genres = []
        # artists = auth.sp.artist(i['track']['artists'])
        # artist_ids = []
        # for j in artists:
        #     artist_ids.append(j['id'])
        # artist_info = auth.sp.artists(artist_ids)
        # for k in artist_info:
        #     genres.append(k['genres'])

        # Obtains other track details
        analysis = auth.sp.audio_features(i['track']['id'])

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

def download_user_playlists():
    '''Downloads user's playlists data'''
    playlists = auth.sp.user_playlists(auth.user_id)

    with open('../Data/user_playlists.json', 'w', encoding='utf-8') as f:
        json.dump(playlists, f)


# Load from local storage section
def load_downloads(playlist_name: str | None):
    '''Loads data from stored file'''
    if not playlist_name:
        with open('../Data/track_dump.json', 'r', encoding='utf-8') as f:
            saved: dict = json.load(f)
        return saved
    else:
        with open(f'../Data/Spotify_Playlists/{playlist_name}.json', 'r', encoding='utf-8') as f:
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
    '''Prints out data saved locally'''
    results: dict = load_downloads(None)
    index = 0
    print('Saved tracks:')
    for index, i in enumerate(results['items']):
        print(index + 1, i['track']['name'])

def load_users_playlists():
    '''Loads data on the user's playists'''
    with open('../Data/user_playlists.json', 'r', encoding='utf-8') as f:
        playlists = json.load(f)
    return playlists

# Upload data to spotify
def write_new_playlist_to_storage(playlist_info:dict):
    '''Saves newly created playlist data locally'''
    with open(f'../Data/New_Playlists/{playlist_info["name"]}.json', 'w', encoding='utf-8') as f:
        json.dump(playlist_info, f, indent=4)

def open_offline(playlist_name):
    '''Adds a playlist to the list of unuploaded playlists'''
    # todo: change to check local playlists directory
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


def upload_new_playlist(playlist_name):
    '''Uploads locally stored playlists to spotify'''
    with open(f'../Data/New_Playlists/{playlist_name}.json', 'r', encoding='utf-8') as f:
        playlist_info = json.load(f)

    print(f'Creating Playlist - "{playlist_name}" Online')
    new_playlist = auth.sp.user_playlist_create(auth.user_id,
                                    name=playlist_info['name'],
                                    public=playlist_info['publicity'],
                                    collaborative=playlist_info['collab'],
                                    description=playlist_info['desc'])
    if new_playlist:
        print(f'Playlist - "{playlist_name}" Created online')
        auth.sp.user_playlist_add_tracks(auth.user_id,
                                    playlist_id=new_playlist['id'],
                                    tracks=playlist_info['track_list'])

        print(f'Here\'s this link: {new_playlist["external_urls"]["spotify"]}')
        remove(f'../Data/New_Playlists/{playlist_name}.json')
    else:
        print('Something went wrong and the songs couldn\'t be added')
