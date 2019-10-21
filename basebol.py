from microbit import *
import antigravity
import music
#   Bilbiography:
#       https://github.com/xepps/microbit-pong/blob/master/pong.js
#       https://github.com/rdagger/micropython-ssd1351/blob/master/demo_sprite.py
#       https://stackoverflow.com/questions/15863858/how-to-make-the-ball-bounce-only-if-it-hits-the-paddle-in-python-pygame-breako
#   Brief:
#       Design a game which is a hybrid of Breakout, Pong and Baseball - where the area layout is in a cup shape, and the goal is determined by
#       North, East, South and West values.
#       The Compass function in the MicroBit is programmed to be the Baseball bat.
#       The (Base) Bol is just one brightened pixel which moves through 2D space.
it = -int(compass.heading()/30)
comp = display.show(Image.ALL_CLOCKS[it])

# Game tells which direction through random.choice() the layout of the playing field,
# and where the goal is located.
arwN = Image.ARROW_N
arwE = Image.ARROW_E
arwS = Image.ARROW_S
arwW = Image.ARROW_W
# Shortened the Image Constructor's set variables.
arrows = [arwN, arwE, arwS, arwW]
# The layouts of each playing field utilizing the custom Image constructor.
nolo = Image("00000:90009:90009:90009:99999")
ealo = Image("99999:90000:90000:90000:99999")
solo = Image("99999:90009:90009:90009:00000")
welo = Image("99999:00009:00009:00009:99999")
# Where the layouts' randomness occurs through a list.
layouts = [nolo,ealo,solo,welo] # [north_layout,east_layout,south_layout,west_layout]
# Where the goals are located, accompanied by "gack" (Goal Acknowledged)
nogo = [[0,4]]
eago = [[4,0]]
wego = [[0,-4]]
sogo = [[-4,0]]
goals = [nogo,eago,sogo,wego] # [north,east,south,west]
gack = False # Goal acknowledge as "gack".
# The Base_Bol class initializing the 2 manipulatable values.
class Base_Bol:
  x = 0
  y = 0
  # Allocates where the Base_Bol class' brightened LED pixel will be
  display.set_pixel(x,y,8)

def bol(self):
  bol_ptr = Base_Bol.x
  Base_Bol.y += bol_ptr
  return bol_ptr
        
# 'bol' properties
bol_direction = [Base_Bol.x,Base_Bol.y] # Take coordinates as indices
# Compass through Clock Matrix LED Display (Image)
while True:
  
  for i in arrows:
    display.show(i)
    sleep(3000)
    for n in layouts:
      display.show(n)
      sleep(9000)
      n = n + 1 # Go through each indices the list
      if n>4:
        n=0
    i = i + 1
    if i>4:
      i=0
  
  if gack is True:
    for i in arrows and n in layouts:
      i=0
      n=0
    gack = False

  if bol_direction>4 or bol_direction>0:
    bol_direction=0 # Set the bol back to 0
    g = 0
    if bol_direction>goals[g]: # If the bol goes past the goal's coordinates
        display.scroll("GOAL!")
        music.play(music.BA_DING)
        g += 1
        if g>4:
          g = 0

  if bol_direction == comp.get_pixel(): # If set_pixel's x-axis and y-axis is equal to the compass needle's x-axis and y-axis:
    if bol_direction==4:
      bol_direction-=1 # Bol direction goes opposite of compass needle/bat intersect.
    if bol_direction==0:
      bol_direction+=1 # Bol direction goes opposite of compass needle/bat intersect.