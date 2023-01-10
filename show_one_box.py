### show bbox in picture ###

import cv2, math

# read file
image = cv2.imread("./name_image.jpg")
# read label 
label = open("./name_label.txt", "r").read() # 1 file 1 box

# split class name and box
class_name, x_center, y_center, width, height  = label.split(" ")
x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)

# get width, height image
height_img, width_img, channel = image.shape

# resize image 
div = height_img / 1080
new_height = math.ceil(height_img / div)
new_width = math.ceil(width_img / div)
reimg = cv2.resize(image, (new_width, new_height))
# convert yolo format 
x_max = math.ceil((x_center*new_width) + (width*new_width)/2)
x_min = math.ceil((x_center*new_width) - (width*new_width)/2)
y_max = math.ceil((y_center*new_height) + (height*new_height)/2)
y_min = math.ceil((y_center*new_height) - (height*new_height)/2)

# create rectangle in image
start = (x_min, y_min)
stop = (x_max, y_max)
reimg = cv2.rectangle(reimg, start, stop, (0,0,255), 5)

# save image .jpg
cv2.imwrite("new_image.jpg",reimg)
# show image
cv2.imshow("Image",reimg)
cv2.waitKey(0)            
cv2.destroyAllWindows()
