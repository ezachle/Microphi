import requests
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#clientID = '278024b7be9d447fbea9d0cc5660b904'
#clientSecret = '5f160c0b60174ee8925f8a67ccf9aab6'
clientID = 'aa836a23666f44d6801955021f69b594'
clientSecret = '58a7f746e05e4dc2b17a7a618f92f5f8'
clientCreds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
musicGet = spotipy.Spotify(client_credentials_manager=clientCreds)
#token = "BQDD-QeuVXJKANN63kbiXzfluifjFL5YS5_WiqmGedz2ogHFaOPcmzUOZBB-E7E5rRohqVZ7eQjYTYuzZqMcjMnut8fcHHSxespajaAsoYXI8IMtD0s3k3Tygm546ryWVg27kKLxfTKP3I_RewLVs9ZWRfC2vhuVGDGyqVeRINh77Zk"
token = util.prompt_for_user_token(username='Studsquito', scope='user-read-currently-playing user-read-playback-state user-modify-playback-state', client_id=clientID, client_secret=clientSecret, redirect_uri='http://localhost/')
def getSongs():
    song = input("Enter a song to search.\n")
    results = musicGet.search(q=song, limit=10)
    songs = {}
    for i, j in enumerate(results['tracks']['items']):
        namen = (j['name'])
        songs[namen] = j['uri']
    return songs
def isPlaying():
    playStuff = []
    currentlyPlaying = spotipy.Spotify(auth=token)
    actualPlaying = currentlyPlaying.currently_playing()
    if actualPlaying is not None:
        game = currentlyPlaying.devices()["devices"]
        game2 = json.dumps(game)[1:-1]
        game2 = game2[0:49] + "}"
        game3 = eval(game2)
        id = game3["id"]
        realPlayer = actualPlaying["is_playing"]
        bruh = actualPlaying["item"]
        title = bruh["name"]
        artist1 = bruh["artists"]
        artist2 = json.dumps(artist1)[1:-1]
        artist2 = artist2[0:280]
        if artist2.endswith("}") != True:
            artist2 = artist2 + "}"
        artist3 = eval(artist2)
        realArt = artist3["name"]
        playin = "Playing " + title + " by " + realArt
        timeStamp = "Currently at " + str(int(actualPlaying["progress_ms"]) // 1000 // 60) + " minutes and " + str(int(actualPlaying["progress_ms"]) / 1000 % 60) + " seconds in the song."
    else:
        realPlayer = actualPlaying
        playin = "Not Playing"
        timeStamp = "Invalid time."
    playStuff.append(playin)
    playStuff.append(timeStamp)
    print(playin)
    print(timeStamp)
    print(realPlayer)
    if realPlayer:
        playing = True
        currentlyPlaying.pause_playback(device_id=id)
    elif not realPlayer:
        playing = False
        currentlyPlaying.start_playback(device_id=id)
    else:
        playing = False
    return playing
def skipSong():
    currentlyPlaying = spotipy.Spotify(auth=token)
    actualPlaying = currentlyPlaying.currently_playing()
    if actualPlaying is not None:
        game = currentlyPlaying.devices()["devices"]
        game2 = json.dumps(game)[1:-1]
        game2 = game2[0:49] + "}"
        game3 = eval(game2)
        id = game3["id"]
        currentlyPlaying.next_track(device_id=id)
def nextSong(theNext):
    currentlyPlaying = spotipy.Spotify(auth=token)
    actualPlaying = currentlyPlaying.currently_playing()
    if actualPlaying is not None:
        game = currentlyPlaying.devices()["devices"]
        game2 = json.dumps(game)[1:-1]
        game2 = game2[0:49] + "}"
        game3 = eval(game2)
        id = game3["id"]
        print(theNext)
        lyst = [theNext]
        currentlyPlaying.start_playback(device_id=id, uris=lyst)