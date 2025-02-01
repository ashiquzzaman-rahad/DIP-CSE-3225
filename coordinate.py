from PIL import Image
import numpy as np

img = Image.open("myimg.png")

x1 = int(input("Enter the upper x of coordinate:"))
y1 = int(input("Enter the upper y of coordinate:"))

x2 = int(input("Enter the lower x of coordinate:"))
y2 = int(input("Enter the lower y of coordinate:"))

arr_img = np.array(img)

crop_rectangle = (x1, y1, x2, y2)
cropped_im = img.crop(crop_rectangle)

cropped_im.show()

for x in range((x2-x1)):
    for y in range((y2-y1)):
        print(arr_img[x][y])


for x in range(x1,x2):
    for y in range(y1, y2):
        arr_img[x][y] = [255, 0,0, 255]
        
img2 = Image.fromarray(arr_img)
img2.show()

