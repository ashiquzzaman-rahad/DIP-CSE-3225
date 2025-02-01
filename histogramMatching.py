import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

import numpy as np
import PIL.Image as im
import matplotlib.pyplot as plt

img2 = im.open('sampleGrey2.jpeg')
img2.show()
img2_arr = np.array(img2)
height2, width2 = img2_arr.shape

x = list(range(256))
histogram_arr2 = np.zeros_like(range(256))

for i in range(height2):
    for j in range(width2):
        histogram_arr2[img2_arr[i,j]] += 1

plt.bar(x, histogram_arr2)
plt.xlabel("Intensity level")
plt.ylabel("Number of pixels")
plt.title("Histogram of the target image intensity")
plt.show()

g = np.zeros_like(range(256))
g[0] = histogram_arr2[0]

for i in range(1,256):
    g[i] += g[i - 1] + histogram_arr2[i]

g = 255 * (g / (height2 * width2))
g = np.array(g, dtype=np.uint64)
print(g)

img = im.open('sampleGrey.jpg')
img.show()
img_arr = np.array(img)
height, width = img_arr.shape

histogram_arr = np.zeros_like(range(256))

for i in range(height):
    for j in range(width):
        histogram_arr[img_arr[i,j]] += 1

plt.bar(x, histogram_arr)
plt.xlabel("Intensity level")
plt.ylabel("Number of pixels")
plt.title("Histogram of the normal image intensity")
plt.show()

s = np.zeros_like(range(256))
s[0] = histogram_arr[0]

for i in range(1,256):
    s[i] += s[i - 1] + histogram_arr[i]

s = 255 * (s / (height * width))
s = np.array(s, dtype=np.uint64)
print(s)

matched_img_arr = np.zeros_like(img_arr)
histogram_matched_arr = np.zeros_like(range(256))
val = 0
val = np.int8(val)
closest_index = 0
closest_values = []

for j in range(len(s)):
    min = 999999
    for i in range(len(g)):
        val = abs(g[i] - s[j])      
        if min < val:
            min = val
            closest_index = i
    closest_values.append(closest_index)

for i in range(height):
    for j in range(width):
        matched_img_arr[i, j] = closest_values[img_arr[i, j]]
        histogram_matched_arr[matched_img_arr[i, j]] += 1

plt.bar(x, histogram_matched_arr)
plt.xlabel("Intensity level")
plt.ylabel("Number of pixels")
plt.title("Histogram of the matched image")
plt.show()

matched_img = im.fromarray(matched_img_arr)
matched_img.show()