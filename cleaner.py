import os
import cv2
import pytesseract
path='jain.jpg'
images=os.listdir(path)
f=open("text.txt","w",encoding="utf-8")
for i in images:
    img=cv2.imread(path+i)
    text=pytesseract.image_to_string(img)
    print("Text Detected from Img",i,text)
    f.write(text)
f.close()


