from PIL import Image, ImageFont, ImageDraw

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


font = ImageFont.truetype("resource/OpenSans-Bold.ttf", 25)
draw = ImageDraw.Draw(background)
text = "Code: 00000128"

position = (10, 10)

temp_image = Image.new("RGB", (bg_height, bg_width), "green")
temp_draw = ImageDraw.Draw(temp_image)
t_left, t_top, t_right, t_bottom = temp_draw.textbbox(position, text, font=font)
position = (bg_height - t_right - 10, 10)

left, top, right, bottom = draw.textbbox(position, text, font=font)
draw.rectangle((left-5, top-5, right+5, bottom+5), fill="black")

draw.text(position, text, font=font, fill="white")


background.show()
