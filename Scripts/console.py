#!/usr/bin/python3
""" console """

import cmd
import shlex  # for splitting the line along spaces except in double quotes
import playlist, algorithms

class VCCommand(cmd.Cmd):
    """ VC console """
    prompt = '(VC) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict


    def do_new(self, arg):
        """Creates a new Playlist"""
        if len(arg) == 0:
            print("** No name given **")
            print('USAGE: create [playlist name]')
            return False

        name = arg
        from_old_playlist = False

        while True:
            mood = input('What mood do you want for it? ').capitalize()
            if mood not in algorithms.moods:
                print('That option isn\'t among the moods available')
                for index, i in enumerate(algorithms.moods.keys()):
                    print(index + 1, i)
                new_mood = input('Do you want to create it [N/Y]? ').lower()
                if new_mood != 'y' and new_mood != 'n' and new_mood != '':
                    print('Please choose Y or N')
                    continue
                if new_mood == 'y':
                    mood_status = self.do_mood(mood)
                    if mood_status == False:
                        print('Unable to create mood (No name given)')
                        continue
                    break
                else:
                    print('You need to choose a mood otherwise it would just add \
                           all the songs to the new playlist')
                    continue
            else:
                break
        print('')

        while True:
            while True:
                strict = input('How strict do you want the selection to be \
                                lax -> strict [1/2/3/4]? ')
                if strict not in ['1', '2', '3', '4']:
                    print('Not a valid strictness level')
                    continue
                strict = int(strict)
                break
            print('')


            print('Selecting songs...')
            tracks = algorithms.select_tracks(mood_name=mood, strictness=strict)
            if len(tracks) == 0:
                print('No tracks match the mood and strictness\n')
                continue
            if len(tracks) == 0 and strict == 1:
                print('You don\'t have any tracks that match this mood')
                return
            break
        print('Selected!\n')

        while True:
            sort_f = input('Should the playlist be sorted [N/Y]?')
            if sort_f != 'y' and sort_f != 'n' and sort_f != '':
                print('Please choose y or n')
                continue
            break

        if sort_f == 'y':
            print('Sorting tracks...')
            sorted_tracks = algorithms.sort_tracks(tracks=tracks, mood=mood)
            if sorted_tracks != KeyError:
                tracks = sorted_tracks
                print('Sorted!\n')
            else:
                print(f'{mood} has no sorting factors')

        while True:
            pub = input('Do you want it to be public [N/Y]? ').lower()
            if pub != 'y' and pub != 'n' and pub != '':
                print('Please choose y or n')
                continue
            if pub == 'y':
                pub = True
            else:
                pub = False
            break

        while True:
            coll = input('Do you want it to be a collaborative playlist [N/Y]? ').lower()
            if coll != 'y' and coll != 'n' and coll != '':
                print('Please choose y or n')
                continue
            if coll == 'y':
                coll = True
            else:
                coll = False
            break

        desc = input('Write a description [OPTIONAL]? ')
        print('')

        print('Creating Playlist...')
        playlist.create_playlist(name=name, tracks=tracks, publicity=pub, collab=coll, desc=desc) # type: ignore (I'm ignoring tis cause it doesn't notice my mood_sf checks)
        if playlist.auth.network_status:
            playlist.data.upload_new_playlist(name)
        else:
            playlist.data.open_offline(name)
            print('Playlist saved offline! Upload on next connection')


    def do_mood(self, arg):
        '''Creates a new mood'''
        args = shlex.split(arg)
        if len(args) == 0:
            print("** No name given **")
            return False
        print('Not yet implemented')


    def do_show(self, arg):
        """Prints out all cached song data"""
        args = shlex.split(arg)
        if len(args) == 0:
            playlist.data.show_saved()


    # def do_new_user(self, arg):
    #     """Deletes an instance based on the class and id"""
    #     args = shlex.split(arg)
    #     if len(args) == 0:
    #         print("** class name missing **")

    def do_sync(self, arg):
        """Updates saved local data"""
        args = shlex.split(arg)

        playlist.auth.network_test()
        if not playlist.auth.network_status:
            return
        while True:
            sync = input('Sync data[Y/N]? ').lower()
            if sync != 'y' and sync != 'n' and sync != '':
                print('Please choose Y or N')
                continue
            break
        if sync == 'n':
            return
        local_playlists = playlist.data.open_offline(None)
        if len(local_playlists) != 0: #type: ignore (should only return a list here)
            print('Uploading local playlists')
            for i in local_playlists: #type: ignore (same reason as above)
                playlist.data.upload_new_playlist(i)
            print('Finished uploading local playlists')

        print('Updating saved data...')
        if len(args) != 0:
            playlist_id = playlist.get_playlist_id(args[0])
            playlist.data.update(playlist_id, args[0])
        else:
            playlist.data.update()
        print('Finished updating saved data')
        print('Sync Complete!')


if __name__ == '__main__':
    if playlist.auth.work_status == 'n':
        exit()
    VCCommand().cmdloop()
