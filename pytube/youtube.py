from pytube import YouTube

# URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream available
video_stream = yt.streams.get_highest_resolution()

# Define the path where the video will be saved
download_path = "path/to/save/video/"

# Download the video
video_stream.download(download_path)

print("Download completed!")
