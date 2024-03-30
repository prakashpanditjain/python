import image
import qrcode
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "I LOVE YOU SO MUCH POOJA"

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill= 'black',back_color = 'White')
img.save('text.png')

# /Users/prakashpandit/PycharmProjects/pythonProject/qrcode_generator.py