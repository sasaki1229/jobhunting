import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API認証と接続（キャッシュ無効）
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='685e8b715dec4d119a8bc56bb8a6adad',
                                               client_secret='200bc27c38944cbd8ae88abf4e6c9478',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='playlist-modify-public',
                                               cache_path='c:\\Users\\丈\\spotify_cache.txt'))

# 特定の曲のトラックIDを入力する
seed_track_id = '7CVug9n4FomAqQV4RCunYv'

# トラック情報を取得する
seed_track_info = sp.track(seed_track_id)

# ダンス可能性（danceability）やエネルギー（energy）などの特徴を取得する
audio_features = sp.audio_features([seed_track_id])
danceability = audio_features[0]['danceability']
energy = audio_features[0]['energy']

# 同じ特徴の曲を検索する
results = sp.recommendations(seed_tracks=[seed_track_id], limit=50, target_danceability=danceability, target_energy=energy)

# 日本語の曲だけを選ぶ
japanese_tracks = []
for result in results['tracks']:
    track_info = sp.track(result['id'])
    if 'JP' in track_info['available_markets']:
        japanese_tracks.append(result['id'])

# 新しいプレイリスト名を生成
new_playlist_name = f'Similar Japanese Tracks Playlist for {seed_track_info["name"]}'


# 重複しないプレイリスト名を作成
counter = 2
while new_playlist_name in [playlist['name'] for playlist in sp.current_user_playlists()['items']]:
    new_playlist_name = f'Similar Japanese Tracks Playlist for {seed_track_info["name"]} {counter}'
    counter += 1

# 新しいプレイリストを作成
user_id = sp.me()['id']  # 現在のユーザーのIDを取得
new_playlist = sp.user_playlist_create(user=user_id, name=new_playlist_name, public=True)
playlist_id = new_playlist['id']

# 選んだ曲をプレイリストに追加
sp.playlist_add_items(playlist_id, japanese_tracks)

# 作成されたプレイリスト名を表示
print("New Playlist Name:", new_playlist_name)
