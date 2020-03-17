import cv2
import pytesseract
import imagecleaner
print(dir(imagecleaner))

f=open("text.txt","w",encoding='utf-16')

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image_dir=[]

img=cv2.imread("C:\\Users\\HP\\Desktop\\opencv-text-recognition\\capture\\img1411.jpg")
text=pytesseract.image_to_string(img)
print(text)
f.write(text)
f.close()

