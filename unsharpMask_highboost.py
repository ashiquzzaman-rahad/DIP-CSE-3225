import numpy as np
import PIL.Image as im

img = im.open('greySmooth.jpg')
img.show()
img_arr = np.array(img)
m,n = img_arr.shape
blur_img_arr = np.zeros_like(img_arr)
mask = np.ones([3, 3], dtype = int) 
# mask = np.array([
#    [0,-1,0],
#     [-1,4,-1],
#     [0,-1,0]
# ])
A = 2

for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = (img_arr[i-1, j-1]*mask[0, 0]+img_arr[i-1, j]*mask[0, 1]+img_arr[i-1, j + 1]*mask[0, 2]+img_arr[i, j-1]*mask[1, 0]+ img_arr[i, j]*mask[1, 1]+img_arr[i, j + 1]*mask[1, 2]+img_arr[i + 1, j-1]*mask[2, 0]+img_arr[i + 1, j]*mask[2, 1]+img_arr[i + 1, j + 1]*mask[2, 2])/9
         
        blur_img_arr[i, j] = img_arr[i,j]+temp


blur_img_arr = blur_img_arr.astype(dtype=np.uint8)
print(blur_img_arr)
unsharpen_masked_img_arr = np.zeros_like(img_arr)
highboost_img_arr = np.zeros_like(img_arr)

Mask = np.zeros_like(img_arr)
for i in range(1, m-1): 
    for j in range(1, n-1):
        Mask[i,j] = abs(img_arr[i, j] - blur_img_arr[i,j])
        highboost_img_arr[i,j] = abs(A*img_arr[i, j] - blur_img_arr[i,j])

for i in range(1, m-1): 
    for j in range(1, n-1):
        unsharpen_masked_img_arr[i,j] = img_arr[i,j] + Mask[i,j]

unsharpen_masked_img_arr = unsharpen_masked_img_arr.astype(dtype=np.uint8)
highboost_img_arr = highboost_img_arr.astype(dtype=np.int8)
print(unsharpen_masked_img_arr)
print(highboost_img_arr)
unsharpen_masked_img = im.fromarray(unsharpen_masked_img_arr)
unsharpen_masked_img.show()
highboost_img = im.fromarray(highboost_img_arr)
highboost_img.show()