# Where user interacts with the spotify client to obtain user_id and authorization token 
import requests
from track import Track

class SpotifyClient:

    def __init__(self, oauth_token, user_id):
        self.__oauth_token = oauth_token
        self.__user_id = user_id
    
    def get_current_user_recent_tracks(self, limit = 10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self.get_api_requests(url)
        response_json = response.json()
        tracks = [Track(track['track']['id'], track['track']['name'], track['track']['artists'][0]['name']) for track in response_json['items']]
        return tracks

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
        response = requests.get(

        )