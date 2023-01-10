### manage dataset ###

import os, shutil

folder_fish = ['pod', 'ku_lare', 'see_kun', 'too', 
                'khang_pan', 'hang_lueang', 'sai_dang', 'sai_dum']
                
# create folder name train and test
if not os.path.isdir("train_dataset"):
    os.makedirs("train_dataset")
if not os.path.isdir("test_dataset"):
    os.makedirs("test_dataset")

big_folder = os.getcwd() # check location path file now

# choose 70 percent for train and 30 percent for test
for name_folder_fish in folder_fish:
    # calculate percent train/test dataset
    sum_item = len(os.listdir(name_folder_fish))
    train_70_percent = int(0.7 * sum_item)
    test_30_percent = sum_item - train_70_percent
    
    # copy to train dataset
    file_train_dataset = sorted(os.listdir(name_folder_fish))[:train_70_percent]
    path_source = big_folder + "\\" + name_folder_fish
    path_train = big_folder + "\\train_dataset"
    
    # move file to folder train dataset
    for fname in file_train_dataset:
        shutil.copy2(os.path.join(path_source,fname), path_train)
        
    # copy to test dataset
    file_test_dataset = sorted(os.listdir(name_folder_fish))[train_70_percent:]
    path_test = big_folder + "\\test_dataset"
    
    # move file to folder test dataset
    for fname in file_test_dataset:
        shutil.copy2(os.path.join(path_source,fname), path_test)
