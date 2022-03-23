import sys
from smbus import SMBus
import time
from colors import Colors
sys.path.append('../lib_oled96')
from lib_oled96 import ssd1306

# init OLED display


class Display:
  def __init__(self):
    self.max_screen_x = 120
    self.max_screen_y = 50
    self.i2cbus = SMBus(1)    
    self.oled = ssd1306(self.i2cbus)
    self.disp = self.oled.canvas
# clear display
  def clear(self):
    self.oled.cls()
    self.oled.display()


  def display_color(self, color):
    self.disp.text(((self.max_screen_x // 2) - 20, self.max_screen_y // 2), f"{color}", fill=1)
    self.oled.display()
    
  def display_start(self):
    self.disp.text(((self.max_screen_x // 2) - 20, self.max_screen_y // 2), f"Press", fill=1)
    self.disp.text(((self.max_screen_x // 2) - 20, self.max_screen_y  // 2 + 10), "any Button",fill=1)
    self.disp.text(((self.max_screen_x // 2) - 20, self.max_screen_y // 2 + 20), "to continue", fill=1)
    self.oled.display()
  
  
