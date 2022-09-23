# before run code please install Duplicate Image Finder >>> pip install difPy
# ref : https://github.com/elisemercury/Duplicate-Image-Finder
# document : https://pypi.org/project/difPy/1.2/
#            https://github.com/elisemercury/Duplicate-Image-Finder/wiki/difPy-Usage-Documentation

from difPy import dif

dif("D:/pic_fish/1image_fish", "D:/pic_fish/2image_fish",similarity="normal", delete=True)

#print(search.result)
#print(search.lower_quality)
#print(search.stats)

