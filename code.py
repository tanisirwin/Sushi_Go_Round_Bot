import ImageGrab
import os
import time
import win32api, win32con

# Notes
# Create a function to "find the game". My idea is to snap shot and store the
# Top left and bottom right corners (10x10) and search for them to calculate
# the area.
# ------------------------------------------------------------------------------------------------------------------
# win32api.mouse_event( dwFlags, dx, dy, dwData )
# dwFlags:
#    win32con.MOUSEEVENTF_LEFTDOWN
#    win32con.MOUSEEVENTF_LEFTUP
#    win32con.MOUSEEVENTF_MIDDLEDOWN
#    win32con.MOUSEEVENTF_MIDDLEUP
#    win32con.MOUSEEVENTF_RIGHTDOWN
#    win32con.MOUSEEVENTF_RIGHTUP
#    win32con.MOUSEEVENTF_WHEEL
# dx and dy:
#    describe the mouse's absolute position along the x and y axis.
#    they use a coordinate system different than the one we've been using.
#    So, we'll leave them set to zero and rely on a different part of the API for our mouse moving needs.
# dwData:
#    This function is used if (and only if) dwFlags contains MOUSEEVENTF_WHEEL.
#    Otherwise is can be omitted or set to zero.
#    dwData specifies the amount of movement on your mouse's scroll wheel.
# ------------------------------------------------------------------------------------------------------------------
# 
# ------------------------------------------------------------------------------------------------------------------
# Global Vars
sleep = .1
x_pad = 1160
y_pad = 138

# Move Mouse ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def mousePos(cord):
    win32api.SetCursorPos( x_pad + cord[0], y_pad + cord[1] )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Left Mouse ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def leftClick():
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTDOWN, 0, 0 )
    time.sleep( sleep )
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTUP, 0, 0 )
    print "Left Clicked"

def leftHold():
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTDOWN, 0, 0 )
    time.sleep( sleep )
    print "Left Holding..."

def leftRelease():
    win32api.mouse_event( win32con.MOUSEEVENTF_LEFTUP, 0, 0 )
    time.sleep( sleep )
    print "Left Released"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Utility ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getCords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+640, y_pad+480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    pass

if __name__ == '__main__':
    main()
