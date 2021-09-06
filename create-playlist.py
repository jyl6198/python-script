from spotifyClient import SpotifyClient

def main():
    authorizationToken = input("Please enter your authorization token: ")
    userID = input("Please enter in your userID: ")
    if not authorizationToken or not userID:
        print("Please try again")
        return -1
    spotify = SpotifyClient(authorizationToken, userID)

    numTracks = int(input("Choose the number of songs played recently that you would like to display (up to 20): "))
    while numTracks > 20:
        numTracks = int(input("Choose the number of songs played recently that you would like to display (up to 20): "))
    lastPlayedTracks = spotify.get_n_recent_tracks(numTracks)

    print("There may be some repetition if you have played a certain song more than once.")
    print("Please do not be alarmed and do not hesitate to choose the same song as a seed for the next prompt!")
    for index, track in enumerate(lastPlayedTracks):
            print(f"{index+1}- {track}")

    seedIndexes = input("Enter up to 5 tracks (by index number) that you would like to use as a seed to generate recommended songs: ")
    while len(seedIndexes.split()) > 5:
        seedIndexes = input("Please list up to 5 indexes of the tracks you would like to use as a seed to generate recommended songs: ")
    seedIndexes = seedIndexes.split()

    seedTracks = [lastPlayedTracks[int(index)-1] for index in seedIndexes]
    reccTracks = spotify.get_recommended_tracks(seedTracks)

    print("These are the recommended songs that will be added to your new playlist:")
    for index, track in enumerate(reccTracks):
        print(f"{index+1}- {track}")

    playlistName = input("Please enter a name for the playlist you will create: ")
    while playlistName is None or not playlistName:
        playlistName = input("Please enter a name for the playlist you will create: ")
    playlist = spotify.create_playlist(playlistName)
    spotify.populate_playlist(playlist, reccTracks)
    print(f"{playlist.name} successfully created & added songs! Have a good one :)")

if __name__ == "__main__":
    main()



