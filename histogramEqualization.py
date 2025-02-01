import numpy as np
import PIL.Image as im
import matplotlib.pyplot as plt

img = im.open('sampleGrey.jpg')
img.show()
img_arr = np.array(img)
height, width = img_arr.shape

histogram_arr = np.zeros_like(range(256))

for i in range(height):
    for j in range(width):
        histogram_arr[img_arr[i,j]] += 1

x = list(range(256))

plt.bar(x, histogram_arr)
plt.xlabel("Intensity level")
plt.ylabel("Number of pixels")
plt.title("Histogram of the normal image")
plt.show()


s = np.zeros_like(range(256))
s[0] = histogram_arr[0]

for i in range(1,256):
    s[i] += s[i - 1] + histogram_arr[i]

s = 255 * (s / (height * width))

plt.bar(x, s)
plt.xlabel("Old intensity level")
plt.ylabel("New intensity level")
plt.title("Histogram of the S")
plt.show()

s = np.array(s, dtype=np.uint8)

equalized_img_arr = np.zeros_like(img_arr)
histogram_equalized_arr = np.zeros_like(range(256))

for i in range(height):
    for j in range(width):
        equalized_img_arr[i, j] = s[img_arr[i,j]];
        histogram_equalized_arr[equalized_img_arr[i,j]] += 1

plt.bar(x, histogram_equalized_arr)
plt.xlabel("Intensity level")
plt.ylabel("Number of pixels")
plt.title("Histogram of the equalized image")
plt.show()


equalized_img = im.fromarray(equalized_img_arr)
print(equalized_img_arr)
equalized_img.show()