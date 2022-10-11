# before run code please install Duplicate Image Finder >>> pip install difPy
# ref : https://github.com/elisemercury/Duplicate-Image-Finder
# document : https://pypi.org/project/difPy/1.2/
#            https://github.com/elisemercury/Duplicate-Image-Finder/wiki/difPy-Usage-Documentation

from difPy import dif

search = dif("path_a", "path_b",similarity="normal", delete=True)

#print(search.result)
#print(search.lower_quality)
#print(search.stats)

