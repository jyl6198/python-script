# Where user interacts with the spotify client to obtain user_id and authorization token 
import requests
import json
from track import Track
from playlist import Playlist

class SpotifyClient:

    def __init__(self, oauth_token, user_id):
        self.__oauth_token = oauth_token
        self.__user_id = user_id
    
    # returns a list of songs/tracks (specified by user or default 20) that the current user recently played
    def get_n_recent_tracks(self, limit = 20):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self.get_api_request(url)
        response_json = response.json()
        tracks = [Track(track['track']['id'], track['track']['name'], track['track']['artists'][0]['name']) for track in response_json['items']]
        return tracks
    
    # based on the seed object, returns a list that contains recommended songs
    def get_recommended_tracks(self, tracks, limit = 20):
        seed_tracks_url = ""
        for seedTrack in tracks:
            seed_tracks_url += seedTrack.id + ","
        seed_tracks_url = seed_tracks_url[:-1]# gets rid of the ending comma
        url = f"https://api.spotify.com/v1/recommendations?seed_tracks={seed_tracks_url}&limit={limit}"
        response = self.get_api_request(url)
        response_json = response.json()
        recc_tracks = [Track(track['id'], track['name'], track['artists'][0]['name']) for track in response_json['tracks']]
        return recc_tracks

    # returns a playlist whose playlist name is provided by the user
    def create_playlist(self, playlistName):
        data = json.dumps({
                "name": playlistName,
                "description": "Recommended songs",
                "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.__user_id}/playlists"
        response = self.post_api_request(url, data)
        response_json = response.json()
        playlistID = response_json['id']
        playlist = Playlist(playlistID, playlistName)
        return playlist

    # populates the created playlist with the recommended songs/tracks   
    def populate_playlist(self, playlist, tracks): 
        track_url_list = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(track_url_list)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self.post_api_request(url, data)
        response_json = response.json()
        return response_json
        
    def get_api_request(self, url):
        response = requests.get(
            url, 
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.__oauth_token}"
            }
        )
        return response

    def post_api_request(self, url, data):
        response = requests.post(
            url,
            data = data,
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.__oauth_token}"
            }
        )
        return response