from PIL import Image 
import numpy as np

img = Image.open("sampleGrey.jpg")
img_arr = np.array(img)

c = 1
gamma = float(input())
img_arr = c * ((img_arr) ** gamma)

# img_arr = np.array(img_arr, dtype=np.uint8)
print(img_arr)
img2 = Image.fromarray(img_arr)
img2.show()
# for i in range(img_arr.shape[0]):
#     for j in range(img_arr.shape[1]):
#         img_arr[i, j] = c * ((img_arr[i, j]) ** gamma)

min_val = np.min(img_arr)
max_val = np.max(img_arr)
img_arr = img_arr - min_val
img_arr = img_arr / max_val - min_val
img_arr = img_arr * 255
img_arr = np.array(img_arr, dtype=np.uint8)

print(img_arr)
img3 = Image.fromarray(img_arr)
img3.show()