#coding:utf-8

from PIL import Image
import sys

input_file  = sys.argv[1]
output_file = input_file.split(".")[0] + "_output.png"
message = sys.argv[2]
input_img = Image.open(input_file)

rgb_img   = input_img.convert("RGB")

size  = rgb_img.size

output_img = Image.new("RGB", size)

for x in xrange(size[0]):
  for y in xrange(size[1]):
    r, g, b = rgb_img.getpixel((x, y))
    r = r if r % 2 == 0 else r - 1

    output_img.putpixel((x, y), (r, g, b))


binary_message = ""
for c in message:
  binary_message += "%08d" % int(format(ord(c), 'b'))

count = 0
length = len(binary_message)
for x in xrange(size[0]):
  for y in xrange(size[1]):
    r, g, b = output_img.getpixel((x, y))
    r += int(binary_message[count])

    output_img.putpixel((x, y), (r, g, b))
    count += 1
    if (length <= count):
      break
  else:
    continue
  break

output_img.save(output_file, "PNG")
