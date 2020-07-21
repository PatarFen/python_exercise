from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

im = Image.open('profile.jpg')

number = 10
dr = ImageDraw.Draw(im)
font = ImageFont.truetype('PAPYRUS.ttf', 34)

dr.text((im.size[0]*0.85, im.size[1]*0.05), str(number), font=font, fill="#ff0000")

im.show()


