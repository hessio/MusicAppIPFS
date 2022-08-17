from flask import Flask, render_template, request, redirect, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import boto3
import os
from s3_functions import list_files, upload_file, show_image
import sys
import time

from pydub import AudioSegment
from pydub.playback import play
import io

app = Flask(__name__)

UPLOAD_FOLDER='static/'

@app.route("/")
def home(): 
    contents = show_songs()
    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    songs = [] 
    for i in contents:
    	
    	data = client.cat(i)
		song = AudioSegment.from_file(io.BytesIO(data), format="mp3")
		songs.append(song)

    return render_template('index.html', songs=songs)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST": 
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        time.sleep(3)
        upload_file(UPLOAD_FOLDER + f"/{f.filename}", BUCKET)
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
