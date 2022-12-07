import cv2, glob
all_fish = ['pod', 'ku_lare', 'see_kun', 'too', 'khang_pan', 'hang_lueang', 'sai_dang', 'sai_dum']
images = []
print("GrayScale Image")
for type_fish in all_fish:
    images_path = glob.glob(f"{type_fish}/*.jpg")
    count_fish = 0
    for img_path in images_path:
        # read image by grayscale
        img = cv2.imread(img_path, 0)
        # use the original name
        img_path = img_path.split("\\")
        name_img = img_path[1]
        # save image grayscale
        cv2.imwrite(name_img, img)
        count_fish += 1
    
    print(str(type_fish) + " " + str(count_fish))
