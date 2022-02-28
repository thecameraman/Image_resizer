import sys
print(sys.executable)
from PIL import Image

# Image.open() can also open other image types
img = Image.open("sword.jpg")
num=int(input("enter the width :"))
num1=int(input("enter the height :"))
resized_img = img.resize((num,num1))
resized_img.save("imjdcopy.jpg")
print("executed")