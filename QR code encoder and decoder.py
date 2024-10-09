#qr code generation
import qrcode
import numpy as np
img="https://www.google.co.in/"
QRcode_file="Myfirst_file.png"
QR_image=qrcode.make(img)
QR_image.save(QRcode_file)
QRdecode_file="QRdecoderfile.png"
qrObject=qrcode.QRCode(version=1,box_size=12)
qrObject.add_data(img)
qrObject.make()
image=qrObject.make_image()
image.save(QRdecode_file)
print(np.array(qrObject.get_matrix()).shape)