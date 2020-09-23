import sense_hat, random, time

"""
Author:Paul Okenne
Purpose: Display Iniials When Keyboard is pressed
"""

B=[0,0,0]
W=[255,255,255] 

sense = sense_hat.SenseHat()


initials=[0 ,0];
initials[0] = [
    B, B, W, W, W, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, W, W, W, B, B,
    B, B, W, B, B, B, B, B,
    B, B, W, B, B, B, B, B,
    B, B, W, B, B, B, B, B,
    B, B, W, B, B, B, B, B,
]


initials[1] = [
    B, B, W, W, W, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, B, B, W, B, B,
    B, B, W, W, W, W, B, B,
]


sense.clear()





####
# Main Loop
####

count=0

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        
        if event.action != 'pressed':
            continue
          
        if event.direction in ['right','left','up','down']:
          sense.set_pixels(initials[count % 2])
          count+=1
        
        
        