from flask import Flask, render_template, request
from pytube import YouTube
import re
import os

app = Flask(__name__)


@app.route("/")

def home():
    return render_template('home.html')

@app.route('/download', methods=['POST']) 

def download():
    download_directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    link = request.form
    result = link['link']
    match1 = re.search("^http(s)?://www.youtube.com/watch\?v=", result)
    match2 = re.search("^http(s)?://youtu.be/", result)
    if match1 or match2:
        url = result
        yt = YouTube(url)
        streams = yt.streams.filter(file_extension='mp4')
        video = streams.get_highest_resolution()
        video.download(download_directory)
        return render_template('download.html',message="Video downloaded successfully!",button="Download another video",title="Success!")
    else:
        return render_template('download.html',message="Incorrect video link",button="Try again",title="Error!")
