from PIL import Image

# opening the image 
image = Image.open("monro.jpg")
red, green, blue= image.split() 

# coordinates
left_bias = 50
right_bias = 50

# working with red channel
red_left_coordinates = (left_bias, 0, red.width, red.height)
red_bias_left = red.crop(red_left_coordinates) 

red_right_coordinates = (0, 0 , red.width-right_bias, red.height)
red_bias_right = red.crop(red_right_coordinates)

image_red_channel = Image.blend(red_bias_left, red_bias_right, 0.5)

# working with blue channel
blue_left_coordinates = (0, 0, blue.width-right_bias, blue.height)
blue_bias_left = blue.crop(blue_left_coordinates) 

blue_right_coordinates = (left_bias, 0 , blue.width, blue.height)
blue_bias_right = blue.crop(blue_right_coordinates)

image_blue_channel = Image.blend(blue_bias_left, blue_bias_right, 0.5)

# working with greem channel
green_coordinates = (left_bias/2, 0, blue.width-(right_bias/2), blue.height)
image_green_channel = blue.crop(green_coordinates) 

# creating a final image
new_image = Image.merge("RGB", (image_red_channel,image_green_channel,image_blue_channel))
new_image.thumbnail((800, 800))
new_image.save("monro_warhol.jpg")