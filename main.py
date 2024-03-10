from flask import Flask, request, redirect, render_template_string
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

app = Flask(__name__)

# Spotify credentials
client_id = 'bae3324038d44ab7a1cc0e9cf53682fb'
client_secret = '3673554b0e3e4e7f8900a9ba435b78be'
redirect_uri = 'http://localhost:8888/callback'
scope = 'user-top-read user-read-recently-played'

# Spotify OAuth
sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

def search_track(sp, track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    result = sp.search(q=query, type='track')
    tracks = result['tracks']['items']
    if tracks:
        track_url = tracks[0]['external_urls']['spotify']
        artist_url = tracks[0]['artists'][0]['external_urls']['spotify'] # Artist's Spotify URL
        return track_url, artist_url
    else:
        return None, None

@app.route('/')
def index():
    return render_template_string("""
        <h1>Welcome</h1>
        <p><a href="{{ url_for('login') }}">Login with Spotify</a></p>
    """)

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    sp = spotipy.Spotify(auth=token_info['access_token'])
    top_tracks = sp.current_user_top_tracks(limit=10)
    seed_tracks = [top_tracks['items'][0]['id']]
    recommendations = sp.recommendations(seed_tracks=seed_tracks, limit=20)

    songs = []
    for track in recommendations['tracks']:
        track_url, artist_url = search_track(sp, track['name'], track['artists'][0]['name'])
        songs.append({'title': track['name'], 
                      'artist': track['artists'][0]['name'],
                      'track_url': track_url,
                      'artist_url': artist_url})


    song_urls = [search_track(sp, song['title'], song['artist']) for song in songs]

    return render_template_string("""
        <html>
        <head>
            <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
        </head>
        <body>
            <div class="container">
                <h1>Recommended Songs</h1>
                <ul>
                {% for song in songs %}
                    <li>
                        <a href="{{ song.track_url }}">{{ song.title }}</a> by 
                        <a href="{{ song.artist_url }}">{{ song.artist }}</a>
                    </li>
                {% endfor %}
                </ul>
                <button onclick="window.location.href=window.location.href" class="button">Get More Recommendations</button>
            </div>
        </body>
        </html>
    """, songs=songs)



if __name__ == '__main__':
    app.run(port=8888)
