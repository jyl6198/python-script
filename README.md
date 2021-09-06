# Create a playlist 

### Function
```
Console-based interaction with the user to create a playlist 
that will be populated by recommended songs based on the 
current user's recently played tracks/songs
```

### Start the program:
Download the 4 python files and run the file "create-playlist"
```
python create-playlist.py
```

### Instructions
Head on over to https://developer.spotify.com/documentation/web-api/reference/ and open the following:
  1) Get Current User's Profile
  2) Create a Playlist
  You can open them by searching them up and clicking on "try in our web console" 
  
## Get the current user's ID: 
After clicking on "try in our web console," select "Get token" and check the following boxes:
  * user-read-private
  * user-read-email
  * user-read-recently-played
Then click on "generate token" and then "Try it" 
You should see the following screen and you will want to save the information next to "id:" 
Please refer to the following image to obtain the user's ID: 
