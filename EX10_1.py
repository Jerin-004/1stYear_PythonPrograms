from PIL import Image, ImageFilter


image = Image.open('flowers.jpeg')


# image = image.resize((round(image.size[0]/2), round(image.size[1]/2)))

# image = image.rotate(145)

resized_img = image.resize((image.width + 50, image.height + 70))

# resized_img.show()


flipped_horizontally_img = image.transpose(Image.FLIP_LEFT_RIGHT)

flipped_vertically_img = image.transpose(Image.FLIP_TOP_BOTTOM)

# flipped_horizontally_img.show()

# flipped_vertically_img.show()

# Crop the image
left = 10
upper = 10
right = image.width - 50
lower = image.height
cropped_img = image.crop((left, upper, right, lower))

# cropped_img.show()
rainbow = Image.open('flowers.jpeg')
img_bw = rainbow.convert('1')

# rainbow.show()
# img_bw.show()
rgb_img = image.convert('RGB')

blurred_img = rgb_img.filter(filter=ImageFilter.BLUR)

blurred_img.show()

print(image.size)
# image.show()