# VibeCheck

The project helps create Spotify playlists according to specific moods. It's designed for every music lover. From those who don’t want to have to get out of the shower because that one track comes on, or those who want to focus on their workout without having to skip through the non-hype songs. The app is designed to specifically use the user's own saved tracks and not just a collection of tracks that Spotify recommends.

[Aricle on LinkedIn](https://www.linkedin.com/posts/nnamdi-anyanwu-719179245_python-project-github-activity-7019107102174388224-bKaN?utm_source=share&utm_medium=member_desktop)

## Features

* Create a new playlist based on the user's mood
* Works Offline

## Table of Content

* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#example-of-use)
* [Bugs](#bugs)
* [Contributing](#authors)
* [License](#license)

## Environment

This project is developed/tested using python3 (version 3.11.1)

## Installation

* Clone this repository: `git clone "https://github.com/Blueking-prime/VibeCheck.git"`
* Access console in VibeCheck directory: `cd VibeCheck/Scripts`
* Run VibeCheck: `./console` and enter command

## File Descriptions

### `Scripts/` directory contains Python scripts used for this project

[console.py](/Scripts/console.py) - the console contains the entry point of the command interpreter.
List of commands this console current supports:

* `EOF` - exits console
* `quit` - exits console
* `help` - Displays supported commands
* `new` - Creates a new playlist
* `show` - Prints out all the tracks in the local database.
* `sync` - Syncs local data with online data
* `mood` - Creates a new mood (CURRENTLY NON-FUNCTIONAL)

[auth.py](/Scripts/auth.py) - Handles authentication and internet connectivity tests

[algorithms.py](/Scripts/algorithms.py) - Handles song sorting and selection algorithms

[data.py](/Scripts/data.py) - Handles local data storage and interactions with Spotify's API

[playlist.py](/Scripts/playlist.py) - Handles playlist creation and manipulation

### `Data/` directory contains File Storage and local data as JSON

[moods.json](/Data/moods.json) - Contains the moods the algorithms use

[moods_sf.json](/Data/moods_sf.json) - Contains the sorting factors for the moods

[track_dump.json](/Data/track_dump.json) - Contains the raw track details from Spotify

[track_info.json](/Data/track_info.json) - Contains song info for the locally saved tracks

[local_playlists.json](/Data/local_playlists.json) - Contains a list of local playlists

[user_playlists.json](/Data/user_playlists.json) - Contains the stored data

## Usage

### new

``` shell
(VC) new {playlist_name}
```

### show

``` shell
(VC) show
```

### sync

``` shell
(VC) sync
```

## Example of use

```
VibeCheck$./console.py
(VC) new Demo
What mood do you want for it? sad
How strict do you want the selection to be                       lax > strict [1/2/3/4]? 3

Selecting songs...
Selected!

Should the playlist be sorted [N/Y]?y
Sorting tracks...
Sorted!

Do you want it to be public [N/Y]?n
Do you want it to be a collaborative playlist [N/Y]? n
Write a description [OPTIONAL]? Here's a short description

Creating Playlist...
Adding songs to playlist...
Creating Playlist - "Demo" Online...
Playlist - "Demo" Created online
Here's the link: https://open.spotify.com/playlist/playlist-id
```

## Bugs

`local_playlists` still needs to be cleared manually after the playlists have been uploaded otherwise will throw an error

## Authors

Nnamdi Anyanwu - [Github](https://github.com/Blueking-prime) / [linkedIn](https://www.linkedin.com/in/nnamdi-anyanwu-719179245/)

## License

Standard MIT license
