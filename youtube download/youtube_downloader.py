from pytubefix import YouTube
from pytubefix import Search
import  os
from import_spotipy import show_tracks , select_a_playlist

def download_url(directory_file:str,playlist_name:str):
    try:
        url = input("Enter the YouTube URL: ")
        yt = YouTube(url)
        print("Title:", yt.title)
        print("views:", yt.views)
        yd = yt.streams.get_audio_only()
        file_location=create_directory(directory_file,playlist_name)
        yd.download(file_location)
        print("Download complete.")
    except Exception as e:
        print("An error occurred:", str(e))
def get_directory_file(playlist_name:str)->str:
        choice=input("Do you want to download that file in a location ? (Y/N) slecting No will automatically add that folder in the desktop: ")
        while(choice!="Y"and choice!="N"):
            choice= input("Pls re-enter Y or N: ")
        if choice=="Y":
           directory_file=input("Enter the exact directory where you want to download the playlist")
        else:
            directory_file=""
        return directory_file
def download_song_in_playlist(directory_file,playlist_name:str,youtube_url:str):#download the youtube_video_to_a_file
    try:
        url = youtube_url
        yt = YouTube(url)
        yd = yt.streams.get_audio_only()
        desktop = real_desktop()
        if directory_file!="":
            try:
                file_location=create_directory(directory_file,playlist_name)#create a folder in that directory with the name of the playlist
                yd.download(file_location)
            except:
                print("The directory was not found so it was moved to the desktop")
                file_location=create_directory(desktop,playlist_name)
                yd.download(file_location)
        else:
            file_location=create_directory(desktop,playlist_name)
            yd.download(file_location)
        print("Download complete.")
    except Exception as e:
        print("An error occurred:", str(e))
def real_desktop():
     home=os.path.expanduser("~")
     one_drive_desktop=os.path.join(home, "OneDrive", "Desktop")
     if os.path.isdir(one_drive_desktop):
            return one_drive_desktop
     else:
         return os.path.join(home, "Desktop")
def create_directory(directory_file: str, name: str):#create a folder in a directory
    directory_path = os.path.join(directory_file, name)
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Directory '{directory_path}' created (or already existed).")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_path}'.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return directory_path
def download_spotify_selected_playlist():
     playlist=select_a_playlist()
     directory_file=get_directory_file(playlist[1])
     for playlist_info in playlist[0]['items']:
          track=playlist_info['track']
          s= Search(f"{track['artists'][0]['name']}, {track['name']}")
          if s.results:
                song_youtube = s.results[0]
                print("song Downloaded:", song_youtube.title)
                download_song_in_playlist(directory_file,playlist[1],song_youtube.watch_url)
          else:
              print(f"{track['name']} not found")
                
              
download_spotify_selected_playlist()