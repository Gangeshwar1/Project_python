from PIL import Image
import os

image_1 = Image.open(r'motor.png')


im_1 = image_1.convert('RGB')

path = 'pdf_images'

if not os.path.isdir("image_to_pdf"):
    os.mkdir("image_to_pdf")


image_list = [im_1]

im_1.save(r'image_to_pdf/motor.pdf', save_all=True, append_images=image_list)



print("directory is created")