from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random
im = Image.open('ic_launcher.png')
print('image: width-%d,height-%d' % (im.size[0], im.size[1]))
w, h = im.size
thum = im.thumbnail((w // 2, h // 2))
im.save('thum.png', 'png')
im_blur = im.filter(ImageFilter.BLUR)
im_blur.save('blur.png', 'png')


def rand_letter():
    return chr(random.randint(65, 90))


def rand_color_bg():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rand_color_text():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))

consolas= ImageFont.truetype('consola.ttf',36)
draw = ImageDraw.Draw(image)

points = [(x, y) for x in range(width) for y in range(height)]

for point in points:
    # print(point)
    draw.point(point, fill=rand_color_bg())

for t in range(4):
    draw.text((60 * t + 10, 10), rand_letter(),font=consolas, fill=rand_color_text())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
