# coding question 1
# is_light  that takes a parameter a tuple named pixle, containing RGB values of a pixel (3 integers) 
# The function should return True if the avergae of the tuple values is greater than or equal to 128. and False if the avg is less than 128. 

# make a tuple list 
pixel = ("255", "200", "0")

# get the average of three integers


def is_light(pixel):
  average = int((pixel[0]+pixel[1]+pixel[2])/3)
  if average>=128:
    return True 
  elif average<128:
    return False 

def avg(pixel):
  average = int((pixel[0]+pixel[1]+pixel[2])/3)
  return average

def green(pixel):
  return pixel[1]

def obama(pixel, original_image, col, row):
  grey_val = int((pixel[0]+pixel[1]+pixel[2])/3)
  if (grey_val > 100):
    original_image.putpixel((col, row), (252, 227, 166))
  elif (grey_val > 70):
    original_image.putpixel((col, row), (112, 150, 158))
  elif (grey_val > 20):
    original_image.putpixel((col, row), (217, 26, 33))
  else:
    original_image.putpixel((col, row), (0, 51, 76))

print(is_light((255,255,255) ))
print(is_light((0, 0, 0) ))

# binarize an image 

# import module for image processing 
from PIL import Image 


# open source and destination images 
#image_input = Image.open("sky.jpg").load()
#image_output = Image.open("sky.jpg")
image_input = Image.open("piazza pic.png").load()
image_output = Image.open("piazza pic.png")
#image_input = Image.open("TurtleFlag.png").load()
#image_output = Image.open("TurtleFlag.png")


width = image_output.width
height = image_output.height

# looping over all the pixels in the image input
for col in range(width):
  for row in range(height):
    #obama(image_input[col, row], image_output, col, row)
# if the pixel is set it to white i 
    if is_light(image_input[col, row]):
      image_output.putpixel((col, row), (avg(image_input[col,row]), green(image_input[col,row]), avg(image_input[col,row])))
# otherwise set it to black 
    else: 
      image_output.putpixel((col, row), (avg(image_input[col,row]),green(image_input[col,row]),avg(image_input[col,row])))


# save the image 

image_output.save("obama.png", "png")
# Q2- create output.png 

# process an image and output a binarized from of this image 
# pixels should be assigned as white color if the avg RGB is >= 128 and black otherwise 