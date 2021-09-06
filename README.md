# Create a Spotify Playlist

### Function
```
Console-based interaction with the user to create a playlist 
that will be populated by recommended songs based on the 
current user's recently played tracks/songs
```

### Instructions
Head on over to https://developer.spotify.com/documentation/web-api/reference/ and open the following:
  1) Get Current User's Profile
  2) Create a Playlist
  You can open them by searching them up and clicking on "try in our web console" 
  
### Get the current user's ID: 
After clicking on "try in our web console," select "Get token" and check the following boxes:
  * user-read-private
  * user-read-email
  * user-read-recently-played
<br>
Then click on "generate token" and then "Try it"<br>
You should see the following screen and you will want to save the information next to "id:"<br>
Please refer to the following image to obtain the user's ID:

![User ID SS](https://github.com/jyl6198/python-script/blob/main/images/userID.png)

### Get the current user's authorization token: 
After clicking on "try in our web console," select "Get token" and checkthe following boxes: 
  * playlist-modify-public
  * playlist-modify-private
  * user-read-recently-played
<br>
Then click on "generate token" but **DO NOT** click on "Try it." Otherwise, you will create an empty playlist<br>
You will want to save the information underneath the "OAuth Token" 
Please refer to the following image to obtain the user's Authorization Token:

![Authorization Token SS](https://github.com/jyl6198/python-script/blob/main/images/authToken.png)


### Start the program:
Download the 4 python files and run the file "create-playlist"
```
python create-playlist.py
```
In the console, enter in the information that you obtained from earlier and follow the prompts shown on the screen
When done correctly, you will see:
```
A list of the songs you recently listened to (up to ~20 songs)
A list of the songs you were recommended (currently set to 20 songs)
A playlist created and populated with recommended songs
```

### Sample playlist I created 
![Console example](https://github.com/jyl6198/python-script/blob/main/images/console-example.png)

![Spotify playlist example](https://github.com/jyl6198/python-script/blob/main/images/spotify-playlist.png)
**Enjoy the generated playlist! :)**
