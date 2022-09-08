import microbit

with open('better_img.txt', 'r') as f:
    content = f.read()
    print(content)

content = content.split("\n")

times_run = 0

while True:

    microbit.display.show(microbit.Image(content[0]))

    if times_run > len(content):
        times_run = 0

    if times_run == -1:
        times_run = 0

    if microbit.button_a.is_pressed():
        times_run -= 1
        microbit.display.show(microbit.Image(content[times_run]))

    if microbit.button_b.is_pressed():
        times_run += 1
        microbit.display.show(microbit.Image(content[times_run]))

    microbit.sleep(2000)
