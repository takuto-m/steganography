#coding:utf-8

from PIL import Image
import sys

input_file  = sys.argv[1]
input_img = Image.open(input_file)

rgb_img   = input_img.convert("RGB")

size  = rgb_img.size

binary_message = ""
message = ""
count = 0

for x in xrange(size[0]):
  for y in xrange(size[1]):
    r, g, b = rgb_img.getpixel((x, y))
    binary_message += str(r % 2)
    count += 1

    if len(binary_message) % 8 == 0:
      message += chr(int(binary_message[count-8:count], 2))

print message
