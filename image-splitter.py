# import Image module
from PIL import Image

# select origin image and grid
image_name = "./assets/test-image.png"
rows = 4
cols = 6

# open image file
with Image.open(image_name) as image:
    # get image height and width
    w, h = image.size
    # calculating crop box size in x and y directions
    crop_size_x=w/cols
    crop_size_y=w/rows
    # iterating to move cropping box over the image
    for i in range(0,rows): # first over rows
        for j in range(0,cols): # then over columns
            # crop image based on box coordinates
            cropped=image.crop(box=(j*crop_size_x,i*crop_size_y,j*crop_size_x+crop_size_x,i*crop_size_y+crop_size_y))
            # save image to output directory
            cropped.save("./output/cropped"+str(i)+str(j)+".png")
            