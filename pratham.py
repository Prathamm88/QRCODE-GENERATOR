import qrcode
from PIL import Image
data = input("ENTER THE DATA YOU WANT TO ENCODE : ")
save = input("ENTER THE NAME OF YOUR FILE : ")
qr = qrcode.QRCode(version=1 ,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = 10 , border = 4 )
qr.add_data(data)
qr.make(fit = True)
image = qr.make_image(fill_color= "black",back_color = "white")
image.save(save)
print("Generated Successfully !")

