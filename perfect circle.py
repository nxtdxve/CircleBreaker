import pyautogui as pg
import math
import keyboard

def find_browser_center():
    screenWidth, screenHeight = pg.size()
    return (screenWidth / 2, screenHeight / 2)

""" def draw_circle():
    # Get the center of the browser window (assuming it's maximized)
    (x, y) = find_browser_center()

    r = 300

    # Move to the starting point of the circle
    pg.moveTo(x + r, y)

    pg.mouseDown()
    for i in range(0, 361, 70): # 70 is the best result but not a perfect circle, 6 is a perfect circle but only gets 99.8% 
        x_pos = x + r * math.cos(math.radians(i))
        y_pos = y + r * math.sin(math.radians(i))
        pg.moveTo(x_pos, y_pos, duration=0.01)
    pg.mouseUp()

print("Press 's' to start drawing. Press 'e' to exit.")

while True:
    if keyboard.is_pressed('s'):
        draw_circle()
    elif keyboard.is_pressed('e'):
        exit()
 """

def draw_shape(degrees_step):
    (x, y) = find_browser_center()
    r = 300
    pg.moveTo(x + r, y)
    pg.mouseDown()
    for i in range(0, 361, degrees_step):
        x_pos = x + r * math.cos(math.radians(i))
        y_pos = y + r * math.sin(math.radians(i))
        pg.moveTo(x_pos, y_pos, duration=0.01)
    pg.mouseUp()

print("Press 's' to draw a shape. Press 'e' to exit.")

while True:
    if keyboard.is_pressed('s'):
        degrees_step = 120  # Adjust for different shapes: 120 for triangle, 90 for square, 72 for pentagon, 60 for a circle; 120 for the best result
        draw_shape(degrees_step)
    elif keyboard.is_pressed('e'):
        exit()
