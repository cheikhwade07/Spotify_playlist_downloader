import spotipy 
from spotipy.oauth2 import SpotifyOAuth 

def show_tracks(results:dict):
    #itterate over results which is a playlist in this context
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32s %s" %
            (i+1, track['artists'][0]['name'], track['name']))

def spotifify_identification():
     scope = 'playlist-read-private'
     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="afc1597614d04a66943024dd80fed279",
            client_secret="7aae355ec6c34760b3080259a424b93b",
            redirect_uri="http://localhost:8888/callback",
            scope=scope
            ))
     return sp
def show_spotify_track():#show track of all your spotify playlist
        sp= spotifify_identification();
        playlists = sp.current_user_playlists()
        user_id = sp.me()['id']
        for playlist in playlists['items']:
                print()
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                tracks = sp.playlist_items(playlist['id'], fields="items,next", additional_types=('tracks', ))
                list_playlist=[]
                show_tracks(tracks)

                while tracks['next']: #in case spotify didn't load all the info this will redirect to the next url
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
def select_a_playlist()->dict:
     sp=spotifify_identification()
     playlists = sp.current_user_playlists()
     user_id = sp.me()['id']
     playlist_list=[]
     for playlist in playlists['items']:
                playlist_list+=[playlist['name']]
     print(playlist_list)
     select= input("Which playlist do you want to select: ")
     while select not in playlist_list:
           select=input("That playlist is not part of your library pls re-enter (Make sure to include all spaces): ")
     index=playlist_list.index(select)
     playlist_selected=playlists['items'][index]
     print(playlist_selected['name'])
     print('  total tracks', playlist_selected['tracks']['total'])
     tracks = sp.playlist_items(playlist_selected['id'], fields="items,next", additional_types=('tracks', ))
     show_tracks(tracks)
     playlist_info=(tracks,playlist_selected['name'])
     return playlist_info

