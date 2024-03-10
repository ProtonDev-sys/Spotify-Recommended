# Spotify Song Recommender Flask App

## Description
This Flask application connects to the Spotify API to fetch and display song recommendations. It uses OAuth for Spotify authentication and provides dynamically updated song recommendations.

## Installation

### Requirements
- Python 3
- Flask
- Spotipy

Install the necessary Python packages by running:
```bash
pip install flask spotipy
```

### Setting Up Spotify API Credentials
1. Register your app at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to get your Client ID and Client Secret.
2. Create a `config.py` file in the root directory of this project.
3. Add your Spotify Client ID and Client Secret to `config.py`:
   ```python
   SPOTIFY_CLIENT_ID = 'your_client_id'
   SPOTIFY_CLIENT_SECRET = 'your_client_secret'
   ```

### Running the App
To start the app, run the following command in the terminal:
```bash
python app.py
```
Open your web browser and navigate to `http://localhost:8888` to use the application.

## Features
- OAuth authentication with Spotify.
- Display song recommendations based on the user's listening history.
- Fetch and display more recommendations on demand.

## Contributions
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).

## Author
Protonn
