### show multi box image ###
# https://albumentations.ai/docs/getting_started/bounding_boxes_augmentation/
# https://towardsdatascience.com/convert-pascal-voc-xml-to-yolo-for-object-detection-f969811ccba5

import cv2, math

def color_class(index_class):
    
    match index_class:
        case "0":
            color = (0,0,0) # pod is black
        case "1":
            color = (255,0,0) # ku_lare is blue
        case "2":
            color = (255,191,0) # see_kun is deep sky blue
        case "3":
            color = (19,69,139) # too is saddle brown
        case "4":
            color = (127,20,255) # khang_pan is deep pink
        case "5":
            color = (0,140,255) # hang_lueang is orange
        case "6":
            color = (0,0,255) # sai_dang is red
        case "7":
            color = (128,0,128) # sai_dum is purple
        case "8":
            color = (0,255,0)
    return color


def visualize_box(img, label):

    h_img, w_img, channel = img.shape 

    for i in label :
        name_class, x_center, y_center, width, height = i.split(" ")
        x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)

        x_min = math.ceil((x_center - width / 2) * w_img)
        y_min = math.ceil((y_center - height /2) * h_img)
        x_max = math.ceil((x_center + width /2) * w_img)
        y_max = math.ceil((y_center + height /2) * h_img)

        color = color_class(name_class)
        # create rectangle in image
        rect_img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color, 5)
        
    # resize image
    reimg = cv2.resize(rect_img, (600, 600))

    cv2.imshow('Image', reimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # name image & label use the same name
    name = "sai_dang"
    num_img = 604
    last_img = 732
    count = 0
    while num_img <= last_img:
        try:
            # read image 
            path_image = f"image/{name}{num_img}.jpg"
            image = cv2.imread(path_image)
            #read label
            path_label = f"label/{name}{num_img}.txt"
            with open(path_label, "r") as f:
                label = f.read().split('\n')
            if label[-1] == "":
                label = label[:-1]
            # show image 
            print(num_img)
            visualize_box(image, label)
            count += 1
        except:pass
        num_img += 1
    print(count)