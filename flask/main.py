from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    ydl_opts = {'outtmpl': 'video.mp4'}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file('video.mp4', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True, debug=True)

# sample url: https://www.youtube.com/watch?v=M3TZx-2G8eY&ab_channel=MadMuscles