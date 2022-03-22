from colors import Colors
from disp import Display
from rounds import Round_system
#from Button_handler import buttons
import time
  
class Game:
  def __init__(self):
    self.disp = display()
  def display_c(self):
    self.disp.display_color()
  def clean_display(self):
    self.disp.clear()
    
    
  def start(self):
    self.clean_display()
    r.round()
  
game = Game()
game.start()
r = Round_system()
try:
  while True:
    time.sleep(0.5)
    
except KeyboardInterrupt:
  game.clean_display()
  print("Bye Bye")