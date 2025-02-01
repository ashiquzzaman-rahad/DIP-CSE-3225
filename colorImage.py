from PIL import Image
import numpy as np

img = Image.open('myimg.png')

img_array = np.array(img)

print("Image array:")
print(img_array)
print("\nImage shape:")
print(img_array.shape)

img2 = Image.fromarray(img_array)
img2.show()