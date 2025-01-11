try:
    import spotipy 
    from spotipy.oauth2 import SpotifyOAuth 
except:
      print("spotipy is not installed go to your command prompt and insert pip install spotipy or search for another way to install it")
      quit()


def show_tracks(results:dict):#show tracks of one of your spotify playlist
    #itterate over results which is a playlist in this context
    for i, item in enumerate(results['items']):
        track = item['track']
        print(
            "   %d %32s %s" %
            (i+1, track['artists'][0]['name'], track['name']))

def spotifify_identification():#!!!!! Take care of the identification process
     scope = 'playlist-read-private'
     """
     To use this script you need to go to https://developer.spotify.com/dashboard create an app ,use http://localhost:8888/callback as the redirect url 
     and copy and paste client_id and client_secret in the following source 
     """
     sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="",
            client_secret="",
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
     for playlist in playlists['items']:#make a list contaning all your playlist name
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

