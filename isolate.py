### extract colors of an image
import cv2
import numpy as np
import os
#set work dir to dir of python file
dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir)
Image_extension = '.JPG'

#find all image files
list_of_images = []
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith(Image_extension):
            rel_dir = os.path.relpath(root, dir)
            list_of_images.append(os.path.join(dir,rel_dir, file))
print(len(list_of_images))
z= 0

with open('results.csv', 'w+') as f:
    for images in list_of_images:
        img = cv2.imread(images) # read image
        print(images)
        #scale image
        scale_percent = 30
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        #set colour boundries 
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_bound = np.array([0, 39, 77])   
        upper_bound = np.array([75, 146, 141])
        #create mask
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        #count number of pixels in mask
        count = cv2.countNonZero(mask)
        #write mask and counts to files
        cv2.imwrite(str(images+'_mask.png'), mask)
        print(count)
        f.write(str(count)+','+str(images)+'\n')

