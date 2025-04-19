# import qrcode
from PIL import Image
import qrcode as qr
# image = qr.make("www.google.com")
# image.save("google_qr_code")

qr = qr.QRCode(version = 1,
error_correction = qr.constants.ERROR_CORRECT_H,
box_size = 10,border=5,)
qr.add_data("www.google.com")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="blue")
img.save("custamize_qrcode")