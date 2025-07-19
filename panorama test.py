import cv2
import glob
import matplotlib.pyplot as plt
import math

#Read images

imagefiles = glob.glob("IDK/*") # Need to figue out let it accsess the correct file
imagefiles.sort()

images = []
for filename in imagefiles:
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img)

num_images = len(images)

# Stitch Images
Stitcher = cv2.Stitcher_create()
status, result = Stitcher.stitch(images)
if status == 0:
    plt.figure(figsize=[30,10])
    plt.imshow(result)