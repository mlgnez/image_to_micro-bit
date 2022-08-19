# image_to_micro-bit
Image encoder for microbits.
=============
Takes 5x5 pixel images and transforms them into something microbits can display.

BEWARE: The only way I've found to connect python to microbits is using the online IDE's provided by BBC and Microsoft. The problem with these IDE's is that you can only use packages built into python, which breaks my code because my code needs PIL, numpy, and requests. So my code won't run on a microbit. The only idea I can think of is saving the encoding image to a file that a seperate .py file reads, which then displays.
