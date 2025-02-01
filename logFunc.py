from PIL import Image
import math
import numpy as np

img = Image.open("sampleGrey.jpg")
img_arr = np.array(img)
img_arr = np.array(img_arr, dtype=np.uint8)
c = 1
for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        img_arr[i,j] = c * math.log(1 + img_arr[i,j])

# img_arr = np.array(img_arr, dtype=np.uint8)
img2 = Image.fromarray(img_arr)
img2.show()

min_val = np.min(img_arr)
max_val = np.max(img_arr)
img_arr = img_arr - min_val
img_arr = img_arr / max_val - min_val
img_arr = img_arr * 255

img_image = np.array(img_arr, dtype=np.uint8)
img3 = Image.fromarray(img_image)
img3.show()

print(img_arr)