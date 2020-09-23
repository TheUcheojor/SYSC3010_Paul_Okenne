from sense_hat import SenseHat
from time import sleep
from random import randint

'''
Author:Paul Okenne
Purpose: Turns on random pixels
'''

sense = SenseHat()
sense.clear() 

while True:

    x=randint(0,7)
    y=randint(0,7)
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    
    sense.set_pixel(x,y,r,g,b)

    sleep(2)
