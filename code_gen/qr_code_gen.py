import segno

qrcode = segno.make('Bismillah', micro=False)
# qrcode.save('bismillah.png')
# qrcode.save('bismillah.txt')
print(qrcode.png_data_uri(scale=12, border=1))
