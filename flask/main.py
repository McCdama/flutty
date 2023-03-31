from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)
class Logger:
    def debug(self, msg):
        #if msg.startswith('[error] '):
        #    self.error(msg)

        def error(self, msg):
            print(msg)

def hook(d):
    if d['status'] == 'downloading':
        print('Downloading...')

    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')

@app.route('/download', methods=['POST'])
def download():
    print("request recieved...")
    url = request.form['url']
    ydl_opts = {
        'outtmpl': 'video.mp4',
        # 'logger': Logger(),
        # 'progress_hooks': [hook],
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file('video.mp4', as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, use_reloader=True, threaded=True, debug=True)

# sample url: https://www.youtube.com/watch?v=M3TZx-2G8eY&ab_channel=MadMuscles