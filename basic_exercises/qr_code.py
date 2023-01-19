import pyqrcode
import png

from pyqrcode import QRCode

address = "https://nadyvocallessons.com/"
url = pyqrcode.create(address)
url.png("camera.png", scale=8)