from PIL import Image

background = Image.open("resource/bg.png")
foreground = Image.open("resource/watermark.png")

bg_size = background.size
bg_height = bg_size[0]
bg_width = bg_size[1]

fg_size = foreground.size
fg_height = fg_size[0]
fg_width = fg_size[1]

height = int(bg_height / 2) - int(fg_height / 2)
width = int(bg_width / 2) - int(fg_width / 2)

background.paste(foreground, (height, width), foreground)
background.show()
