''' 
!!!!!! before run code !!!!!!
please put image fish to match the type of fish
'''

import shutil, os
from difPy import dif

''' number fish name '''
num_hang_lueang = 1359
num_khang_pan = 1302
num_ku_lare = 1408
num_pod = 1374
num_sai_dang = 1734
num_sai_dum = 1360
num_see_kun = 1456
num_too = 1360
num_er = 175
num_mix = 569
num_bg = 55

count_all = 0
folder = os.getcwd() # check location path file now
list_fish = ['pod', 'ku_lare', 'see_kun', 'too',
         'khang_pan', 'hang_lueang', 'sai_dang', 'sai_dum', 
         'bg', 'er', 'mix']


def create_folder(name):
    rename_image = "rename_" + name
    if not os.path.isdir(rename_image):
        os.makedirs(rename_image)
        print(f"create new rename {name}")

def check_image(name):
    path_check_folder = folder + "\\" + name
    check_folder = dif(path_check_folder, similarity="normal")
    #print(check_folder.result)

def change_name(oldname, name, num_fish):
    path_new = folder + "\\" + name + "\\" + name + str(num_fish) + ".jpg"
    path_old = folder + "\\" + name + "\\" + oldname
    try:
        os.rename(path_old, path_new)
    except:
        print(num_fish, path_old, path_new)

def move_file(name):
    scr = folder + "\\" + name
    trg = folder + "\\" + "rename_" + name
    files = os.listdir(scr)
    for fname in files:
        try:
            shutil.move(os.path.join(scr,fname), trg)
        except:pass



for namefish in list_fish:
    try:
        ''' check image in folder '''
        check_image(namefish)

        match namefish:
            case "pod":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_pod
                    change_name(filename ,namefish, v)
            case "ku_lare":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_ku_lare
                    change_name(filename ,namefish, v)
            case "see_kun":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_see_kun
                    change_name(filename ,namefish, v)
            case "too":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_too
                    change_name(filename ,namefish, v)
            case "khang_pan":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_khang_pan
                    change_name(filename ,namefish, v)
            case "hang_lueang":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_hang_lueang
                    change_name(filename ,namefish, v)
            case "sai_dang":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_sai_dang
                    change_name(filename ,namefish, v)
            case "sai_dum":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_sai_dum
                    change_name(filename ,namefish, v)
            case "er":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_er
                    change_name(filename ,namefish, v)
            case "mix":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_mix
                    change_name(filename ,namefish, v)
            case "bg":
                for p, filename in enumerate(os.listdir(namefish)):
                    p += 1
                    v = p + num_bg
                    change_name(filename ,namefish, v)

        ''' count fish in folder'''
        count_fish = len(os.listdir(namefish))
        count_all += count_fish
        print(namefish + " : " + str(count_fish))


        ''' create folder if you want to move file '''
        #create_folder(namefish)

        ''' move file '''
        #move_file(namefish)
    except:pass

print("sum fish : " + str(count_all))