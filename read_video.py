import cv2, os

num = 0
limit_img = 100
name_folder = "img"
cap = cv2.VideoCapture("video.mp4") 

# crate new folder 
if not os.path.isdir(name_folder):
    os.makedirs(name_folder)

while (cap.isOpened) and num <= limit_img:
    # read video 
    check, frame = cap.read()
    # check video is not finish
    if check == True:
        # save file image
        cv2.imwrite(f"{name_folder}/IMG{num}.jpg", frame)
    else:
        break
    num += 1
    
cap.release()
