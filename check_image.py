# before run code please install Duplicate Image Folder "difPy"
# ref : https://github.com/elisemercury/Duplicate-Image-Finder
# pip install difPy

from difPy import dif

search = dif("path_folder_imageA", "path_folder_imageB")

print(search.result) # compare the image 2 folder show duplicate images

