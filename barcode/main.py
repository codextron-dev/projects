import barcode

from barcode.writer import ImageWriter

code = barcode.get('code128', '1234567890', writer=ImageWriter())

code.save('my_barcode')