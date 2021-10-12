'''                           -----------------------------
                            -: Qr code using python :- 
                           -----------------------------'''
# First Import QRCode from pyqrcode Module
# Import pngso that you save qr code in png format
import pyqrcode
import png
from pyqrcode import QRCode
 
s = "https://github.com/v1nc1d4/Hacktoberfest2021"

url = pyqrcode.create(s)

# Create and save the svg file naming "QR.svg"
url.svg("QR.svg", scale = 8)

# Create and save the png file naming "QR.png"
url.png('QR.png', scale = 6)
