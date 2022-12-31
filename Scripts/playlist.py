#!/usr/bin/python3
'''The playlist creation module module'''
import auth
import data


def create_playlist(name:str, tracks:dict, publicity:bool=False, collab:bool=False, desc:str=''):
    '''Creates a new playlist locally'''
    track_list = []
    # Extracts ids from the track dict
    print('Adding songs to playlist...')
    for i in tracks:
        track_list.append(i)
    playlist_data = {
                     'name': name,
                     'track_list': track_list,
                     'publicity': publicity,
                     'collab':collab,
                     'desc':desc
                    }
    data.write_new_playlist_to_storage(playlist_data)

def get_playlist_id(playlist_name:str|None):
    '''Gets the id of the playlist'''
    playlist_id = None
    playlists = data.load_users_playlists()
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
