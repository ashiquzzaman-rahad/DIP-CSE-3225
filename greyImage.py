from PIL import Image
import numpy as np

img = Image.open('gray.jpeg').convert('L')
img.show()

img_array = np.array(img)
print(img_array)

img2 = Image.fromarray(img_array)
img2.save("sampleGrey2.jpeg")