import PIL.Image
from PIL import Image
import os

def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "/" + image
            surface_list.append(full_path)
    return surface_list

def s2(path):
    for k, i in enumerate(path):
        im = Image.open(i)
        new_img = im.crop((6, 0, 24, 36))
        new_img.save(f"{'/'.join(i.split('/')[0:2])}/{k}.png")

def s1(path):
    im = Image.open(path)
    for k, i in enumerate(range(128, 897, 128)):
        new_img = im.crop((i - 128, 0, i, 36))
        new_img.save(f"{'/'.join(path.split('/')[0:2])}/{k}.png")

def tr(path):
    for i in path:
        im = Image.open(i)
        im = im.resize((36, 36), PIL.Image.LANCZOS)
        im.save(i)

s2(import_folder("Hero/walk"))
