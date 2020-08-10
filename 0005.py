#iphone 5's screen resolution is 1136*640
from os import walk
from PIL import Image
import os

_resolu_width = 640
_resolu_height = 1136
_root_path = '/Users/peter/Desktop/python_exercise'
_destination = '/Users/peter/Desktop/python_exercise/img/edited/'

def catch_img(path):
    img_names = []

    for dirpath, dirnames, filenames in walk(path):
        img_names.extend(filenames)
        break
    return img_names

def adjust_resolu(data):
    for img in data:
        image = Image.open(os.path.join(_root_path,"img",img))
        if image.size[0] <= _resolu_width and image.size[1] <= _resolu_height:
            print("Not need to re-scale the imag, it can fit in Iphone 5")
        else:
            image.thumbnail((_resolu_width,_resolu_height))
            image.save(_destination + img[:-4]+"_edited.jpg")

if __name__ == "__main__":  
   img_db ='/Users/peter/Desktop/python_exercise/img'
   img_list = catch_img(img_db)
   print(img_list)
   adjust_resolu(img_list)



