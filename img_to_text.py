import pytesseract
import name_check
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img=Image.open('image.jpg')
text=pytesseract.image_to_string(img)
file1=open(r"D:\Sharv\JAVA\\2.txt", "a")
file1.writelines(text)
file1.close()
name_check.check()
