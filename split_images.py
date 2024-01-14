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
        new_img = im.crop((2, 0, 24, 36))
        new_img.save(f"{'/'.join(i.split('/')[0:2])}/{k}.png")

def s1(path):
    k = 0
    im = Image.open(path)
    for j in range(80, 321, 80):
        for i in (range(80, 241, 80)):
            new_img = im.crop((i - 80, j - 80, i, j))
            new_img.save(f"{'/'.join(path.split('/')[0:2])}/{k}.png")
            k += 1

def tr(path):
    for i in path:
        im = Image.open(i)
        im = im.resize((36, 36), PIL.Image.LANCZOS)
        im.save(i)

s1("third_level_materials/wizard/F1uWk1.png")
