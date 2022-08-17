import microbit
from io import BytesIO

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
        bet_img.append(int(img[x][3] / 28))
    else:
        bet_img.append(0)

add_to = ""
timesrun = 0
for x in range(int(len(bet_img) / 5)):

    print(add_to)
    for x2 in range(int(len(bet_img) / 5)):
        add_to += str(bet_img[((x * 5) + x2)])
        print(add_to)
    timesrun += 1
    if add_to != "":
        if timesrun != 5:
            better_img.append(add_to + ":")
        else:
            better_img.append(add_to)
    add_to = ""

print(img)
print(bet_img)
print(better_img)

microimage = microbit.Image(better_img[0],better_img[1],better_img[2],better_img[3],better_img[4])

while True:

    microbit.display.show()
    if microbit.button_a.is_pressed(): #scroll to another image
    if microbit.button_b.is_pressed(): #scroll to another image
    #microbit.sleep(2000)
