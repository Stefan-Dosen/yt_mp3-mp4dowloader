import yt_dlp

url = input("Enter a yt link (single video or playlist): ")
output_type = input("Enter output type (mp4 or mp3): ")

if output_type == 'mp4':
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
    }
elif output_type == 'mp3':
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
else:
    print("Invalid output type, please enter 'mp4' or 'mp3'.")
    exit()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    # Check if playlist and print info if so
    info = ydl.extract_info(url, download=False)
    if 'entries' in info:
        print(f"Playlist title: {info.get('title')}")
        print(f"Number of videos: {len(info['entries'])}")
    # Download (yt_dlp will handle playlists or single videos automatically)
    ydl.download([url])
