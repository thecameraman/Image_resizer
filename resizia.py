print("1.png to jpg")
print("2.jpg to png")
cn = input("Enter choice for types of coversion(1/2/3):")
if cn=='1':
    for file in glob.glob("*.png"):
     print("Image selecetd is =",file)
     choice = input("Enter choice for continuation(Y/N):")
     if choice=='Y':
         im = Image.open(file)
         rgb_im = im.convert('RGB')
         rgb_im.save(file.replace("png", "jpg"), quality=95)
         print ("Executed")
     else:
         print("Thank you for using me")
elif cn=='2':
    for file in glob.glob("*.jpg"):
     print("Image selecetd is =",file)
     choice = input("Enter choice for continuation(Y/N):")
     if choice=='Y':
         im = Image.open(file)
         rgb_im = im.convert('RGB')
         rgb_im.save(file.replace("jpg", "png"), quality=95)
         print ("Executed")
     else:
         print("Thank your for using me")
else:
    print("Error occured")