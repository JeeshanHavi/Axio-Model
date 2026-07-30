import webbrowser
from pytube import Search

def play_music(user):
    music_query = user
    search = Search(music_query)
    
    if search.results:
        # Get the first result
        video = search.results[0]
        print(f"Playing: {video.title}")
    
        webbrowser.open(video.watch_url)
    else:
        print("No results found for your query.")
