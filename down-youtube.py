import yt_dlp

def download_youtube_as_mp3(video_url, output_path="downloads", keep_video=False):
    if keep_video:
        format_option = 'bestvideo+bestaudio/best'
    else:
        format_option = 'bestaudio/best'

    ydl_opts = {
        'format': format_option,
        'keepvideo': keep_video,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

url = "https://www.youtube.com/watch?v=Bd4gxNpbJGE"
download_youtube_as_mp3(url, keep_video=True)
