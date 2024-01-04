from PIL import Image
import os
def import_folder(path):
    surface_list = []
    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + "/" + image
            surface_list.append(full_path)
    return surface_list

def s(path):
    for k, i in enumerate(path):
        im = Image.open(i)
        new_img = im.crop((0, 12, 24, 48))
        new_img.save(f"{'/'.join(i.split('/')[0:2])}/{k}.png")

s(import_folder("Hero/walk"))
