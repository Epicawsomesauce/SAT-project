import cv2
import glob
import matplotlib.pyplot as plt
import math

#Read images

imagefiles = glob.glob("Panorama test/*") # Need to figue out let it accsess the correct file
imagefiles.sort()

images = []
for filename in imagefiles:
    img = cv2.imread(filename)
    print(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)

num_images = len(images)

plt.figure(figsize=[30,10])
num_cols = 3
num_rows = math.ceil(num_images / num_cols)
for i in range(0, num_images):
    plt.subplot(num_rows, num_cols, i+1)
    plt.axis('off')
    plt.imshow(images[i])
#plt.show()


# Stitch Images
Stitcher = cv2.Stitcher_create()
status, result = Stitcher.stitch(images)
status = 0
#if status == 0:
   # plt.figure(figsize=[30,10])
    #plt.imshow(result)
plt.show()