from PIL import Image, ImageOps

img = Image.open("myimg.png")

new_size = (300,300)
resized_img = img.resize(new_size)
resized_img.save("resized.png")

img = img.convert('RGB')
img.save("formatcng.jpg", 'JPEG')

# invertImg = ImageOps.invert(img)
# invertImg.save('invert.png')
# invertImg.show()
