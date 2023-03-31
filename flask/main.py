from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

def download_video(url, filename):
    ydl_opts = {
        'outtmpl': filename,
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-n', '16']
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/download', methods=['POST'])
def start_download():
    url = request.form['url']
    video_title = yt_dlp.YoutubeDL().extract_info(url, download=False).get('title', 'video')
    filename = f"{video_title}.mp4"
    download_video.delay(url, filename)
    return f"Downloading {video_title}..."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True, debug=True)
