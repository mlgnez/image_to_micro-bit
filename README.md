Image encoder for microbits.
=============
Takes 5x5 pixel images and encodes them into a matrice that the microbit reads as a custom image.

INSTRUCTIONS: (this is the way I got this to work)
1. Create a new pycharm project and github repo.
2. Add these files to the project and the repo.
3. Change line 7 of square.py to the link to the images in your repo. (You need to run square.py for each image and change line 7 each time with the image link | This will add to better_img.txt, which is what microbit_square.py reads and displays.)
4. Open https://python.microbit.org/v/2
5. Connect your microbit.
6. Copy and paste the code from "microbit_square.py" into the editor.
7. Flash to the microbit.
8. Go into pycharm, and at the bottom click on the terminal tab.
9. Input 'ufs put better_img.txt' (without the '' btw)
(optional) 8A. Input ufs ls (this shows all files on the microbit. It should main.py and better_img.txt)
10. Press the black button on the back top of the microbit. This will re-fresh the program on the microbit, which will now not show a sad face and an error, but instead the first image. Then, press a or b to go forward or back in the image slideshow. (This requires that you have done #3 atleast once to get 1 image. To get multiple images, do #3 multiple times with multiple images.)
