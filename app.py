from flask import Flask, render_template,send_file
import pytesseract
import cv2
import os
app=Flask(__name__)
image_dir="C:\\Users\\HP\\Desktop\\Tesseract OCR\\static\\data\\images\\"
audio_dir="C:\\Users\\HP\\Desktop\\Tesseract OCR\\static\\data\\audio\\"
video_dir="C:\\Users\\HP\\Desktop\\Tesseract OCR\\static\\data\\video\\"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/<page>')
def page(page):
    return render_template(page)
@app.route('/data/images/<image>')
def fetch(image):
    img=cv2.imread(image_dir+image)
    text=pytesseract.image_to_string(img)
    print(text)
    return send_file(image_dir+image,mimetype="image/*"),"<b>"+text+"</b>"
@app.route('/data/audio/<audios>')
def fetch_audio(audios):
    return send_file(audio_dir+audios,mimetype="audio/*")
@app.route('/data/video/<videos>')
def fetch_video(videos):
    return send_file(video_dir+videos,mimetype="video/*")    


app.run(port=80)