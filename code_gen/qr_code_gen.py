import segno
#
qrcode = segno.make('Jagoron CST: 3rd')
qrcode.save('jagoron.png')
# qrcode.save('bismillah.txt')
print(qrcode.png_data_uri(scale=12, border=1))


#
# EAN = barcode.get_barcode_class('ean13')
# my_ean = EAN('5901234123457', writer=ImageWriter())
# fullname = my_ean.save('ean13_barcode')
