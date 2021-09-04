class Track:

    def __init__(self, id, name, artist):
        self.id = id
        self.name = name
        self.artist = artist
    
    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"
    
    def __str__(self):
        return self.name + " by " + self.artist