import qrcode
from PIL import Image

qr = qrcode.QRCode(version =1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size= 10, border= 5,)

qr.add_data("Link")
qr.make(fit = True)
img = qr.make_image(fill_color="pink",back_color="white")
img.save("Name.png")