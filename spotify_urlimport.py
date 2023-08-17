def extract_track_id(url):
    # URLからトラックIDを抽出
    start_index = url.find("track/") + len("track/")
    end_index = url.find("?si=")
    if start_index != -1 and end_index != -1:
        track_id = url[start_index:end_index]
        return track_id
    else:
        return None

def main():
    # ユーザーがURLを入力する
    spotify_url = input("SpotifyのURLを入力してください: ")

    # トラックIDを抜き出す
    track_id = extract_track_id(spotify_url)
    if track_id:
        print("抜き出されたトラックID:", track_id)
    else:
        print("トラックIDが見つかりませんでした。")

if __name__ == "__main__":
    main()
