import numpy as np
import PIL.Image as im

img = im.open('greyImage.jpg')
img.show()
img_arr = np.array(img)
m,n = img_arr.shape
blur_img_arr = np.zeros_like(img_arr)
mask = np.ones([3, 3], dtype = int) 
# mask = np.array([
#     [0,1,0],
#     [1,2,1],
#     [0,1,0]
# ])
mask = mask / 9

for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = img_arr[i-1, j-1]*mask[0, 0]+img_arr[i-1, j]*mask[0, 1]+img_arr[i-1, j + 1]*mask[0, 2]+img_arr[i, j-1]*mask[1, 0]+ img_arr[i, j]*mask[1, 1]+img_arr[i, j + 1]*mask[1, 2]+img_arr[i + 1, j-1]*mask[2, 0]+img_arr[i + 1, j]*mask[2, 1]+img_arr[i + 1, j + 1]*mask[2, 2] 
         
        blur_img_arr[i, j] = temp


blur_img_arr = blur_img_arr.astype(dtype=np.uint8)
print(blur_img_arr)
blur_img = im.fromarray(blur_img_arr)
blur_img.show()
        
        
