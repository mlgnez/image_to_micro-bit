import microbit
from io import BytesIO

import microbit
from PIL import Image as PILImage
from numpy import *
import requests

response = requests.get("https://raw.githubusercontent.com/mlgnez/image_to_micro-bit/main/5x5.png")
pil_img = PILImage.open(BytesIO(response.content))

img = list(pil_img.getdata())
bet_img = []
better_img = []

for x in range(int(len(img))):
    if img[x][3] != 0:
        add_up = 0
        for x2 in range(4):
            add_up += int(img[x][x2-1])
        bet_img.append(int(img[x][3] / (add_up / 9)))
    else:
        bet_img.append(0)

add_to = ""
times_run = 0
for x in range(int(len(bet_img) / 5)):

    print(add_to)
    for x2 in range(int(len(bet_img) / 5)):
        add_to += str(bet_img[((x * 5) + x2)])
        print(add_to)
    times_run += 1
    if add_to != "":
        if times_run == 5:
            better_img.append(add_to)
        else:
            add_to += ":"

print(img)
print(bet_img)
print(better_img)

microimage = microbit.Image(better_img[0])

while True:

    microbit.display.show(microimage)
    #if microbit.button_a.is_pressed(): #scroll to another image
    #if microbit.button_b.is_pressed(): #scroll to another image
    microbit.sleep(2000)
