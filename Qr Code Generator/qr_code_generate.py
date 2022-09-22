import qrcode
import os 
import datetime

input_URL = "https://www.google.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)
# For creating directory
if not os.path.isdir("qr_images"):
    os.mkdir("qr_images")

qr.add_data(input_URL)
qr.make(fit=True)

# unique file name
# import uuid
# filename = str(uuid.uuid4())
#qr_img = filename+'.png'
 
img = qr.make_image(fill_color="black", back_color="white")
# Store Images in Directory folder
# img.save("qr_images/"+qr_img)
img.save("qr_images/qr.png")


print("QR code generated successfully")