YouTube Downloader with yt-dlp
This is a small Python script that lets you download videos or audio from YouTube using yt-dlp. You can choose to download either the best quality video as an MP4 file or just the audio as an MP3.

Before you run the script, make sure you have Python installed and the yt-dlp package available.

Important:
This script requires ffmpeg to be installed on your system because yt-dlp uses it to process and convert media files. You need to download ffmpeg yourself and add its bin folder to your system's PATH environment variable. Without this, audio extraction and format conversion won’t work.

If you don’t have ffmpeg installed or haven’t added it to your PATH, the script will show an error saying it can’t find ffmpeg.
Here's a link to download it: https://www.gyan.dev/ffmpeg/builds/
Download the ffmpeg-2025-06-16-git-e6fb8f373-full_build.7z file

Once everything is set up, run the script and enter the YouTube link and the output type (mp4 or mp3). The files will be saved in the Downloads folder where you run the script.
