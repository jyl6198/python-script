class Track:

    def __init__(self, id, name, artist):
        self.id = id
        self.name = name
        self.artist = artist
    
    def create_playlist(self):
        return -1
    
    def __str__(self):
        return self.name + " by " + self.artist