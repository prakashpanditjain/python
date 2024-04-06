import image
import qrcode
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)

data = "https://www.youtube.com/watch?v=yAF6CzAAL3s"

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill= 'black',back_color = 'white')
img.show()
# img.save('text.png')

# /Users/prakashpandit/PycharmProjects/pythonProject/qrcode_generator.py