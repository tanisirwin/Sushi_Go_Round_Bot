import ImageGrab
import os
import time

# Notes
# Create a function to "find the game". My idea is to snap shot and store the
# Top left and bottom right corners (10x10) and search for them to calculate
# the area.
# ------------------------------------------------------------------------------------------------------------------

# Global Vars
x_pad = 1160
y_pad = 138

def screenGrab():
    box = ( x_pad+1, y_pad+1, x_pad+640, y_pad+480 )
    im = ImageGrab.grab( box )
    im.save( os.getcwd() + '\\full_snap__' + str( int( time.time() ) ) + '.png', 'PNG' )

def main():
    screenGrab()

if __name__ == '__main__':
    main()
