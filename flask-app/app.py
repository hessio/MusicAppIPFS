from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import boto3
import os
from s3_functions import upload_file, show_songs
import sys
import time
import subprocess
from pydub import AudioSegment
from pydub.playback import play
import io
import sys
import time
sys.path.append('/path/to/ffmpeg')

app = Flask(__name__)

UPLOAD_FOLDER='flask-app/static/'

@app.route("/")
def home(): 
    contents = ['one.mp3','two.mp3', 'file_example_MP3_1MG.mp3', 'three.mp3'] #show_songs()
    #client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    songs = [] 
    for i in contents:
        #data = client.cat(i)import subprocess
        #result = subprocess.run(['ipfs', 'cat', i], stdout=subprocess.PIPE)
        #print(result, file=sys.stderr)
        #data = result.stdout
        #song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
        songs.append(i)
        
    return render_template('index.html', songs=songs)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST": 
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        time.sleep(3)
        upload_file(UPLOAD_FOLDER + f"/{f.filename}")
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
