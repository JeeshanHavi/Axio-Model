import webbrowser
from urllib.parse import quote

def play_music(song: str):
    song = song.strip()

    if not song:
        print("Please enter a song name.")
        return

    url = f"https://www.youtube.com/results?search_query={quote(song)}"

    print(f"Searching YouTube for: {song}")
    webbrowser.open(url)

if __name__ == "__main__":
    song = input("Enter song name: ")
    play_music(song)
