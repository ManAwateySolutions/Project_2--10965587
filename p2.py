import qrcode 
import PySimpleGUI as psg
layout = [
    
[psg.Input(" ", key = 'INPUT_1')],
[psg.Button('Genetate QR code', key = 'create_QRcode')],
[psg.Image('paler.jpeg')]
    
]

window = psg.Window('Quick response code (QR Code) Generator ', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    if event == 'create_QRcode':
        input_1 = values['INPUT_1']
        image = qrcode.QRCode(
            version = None, 
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            border=10, 
            box_size=12
        )
        image.add_data(input_1)
        image.make(fit = True)
        FILL_COLOR = (200, 18, 52)
        BACK_COLOR = (10, 45, 30)
        img = image.make_image(fill_color = 'black', back_color = 'red')
        img.save('paler.jpeg')

        
window.close()
# NOTE: Every qr code generates after the next imput has been run.

"""
NAME: AWATET MANASSEH ADDOR
ID: 10965587
"""