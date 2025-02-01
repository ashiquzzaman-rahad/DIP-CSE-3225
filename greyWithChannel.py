from PIL import Image
import numpy as np
import cv2

img = cv2.imread("smothImg.png")
blue, green, red = cv2.split(img)

grayscale = (red * 0.1) + (green * 0.1) + (blue * 0.8)

grayscale = grayscale.astype(np.uint8) 

arr = np.array(grayscale)
print(arr)

img2 = Image.fromarray(arr)

img2.show()
img2.save("greySmooth.jpg")