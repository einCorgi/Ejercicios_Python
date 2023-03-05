# Let's import the/our libraries <||> Importamos nuestra(s) biblioteca(s)
# If you are working in Pycharm you should probably use the pillow library
import qrcode

# Let´s declare the QR image features <||> Declaremos las caracteristicas de la imagen QR
features = qrcode.QRCode(version=1, box_size=40, border=3)
# Let´s declare our web address related to our image <||> Declaramos la dirección web relacionada a nuestra imagen
features.add_data("https://github.com/einCorgi/Agente_Lenguaje_Natural/tree/main")
# Unknow description but necessary implementation
features.make(fit=True)

# Let´s generate our image & export it as .png
generate_image = features.make_image(fill_color="black", back_color="white")
generate_image.save("CNN.png")