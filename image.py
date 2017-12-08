from PIL import Image

im = Image.open('image.jpg')
print('image: width-%d,height-%d' % (im.size[0], im.size[1]))
w, h = im.size
