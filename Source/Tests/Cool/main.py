from colors import Colors
from disp import Display
from gpiozero import LED, Button as button
import time
  
  
button1 = button(23)
button2 = button(24)
button3 = button(25)
button4 = button(17)
button5 = button(27)

red = LED(22)
blue = LED(10)
green = LED(9)
white = LED(11)
yellow = LED(5)

  
class Game:
  def __init__(self):
    self.disp = Display()
    self.c = Colors()
    self.level = 0
    self.state = "Start"
  def display_c(self):
    self.disp.display_color(self.c.get_color())
  def clean_display(self):
    self.disp.clear()
    
    
  def start(self):
    self.clean_display()
    self.round_system()
    self.disp.display_start()
    
  def round_system(self):
    self.clean_display()
    if self.state == "Play":
      self.c.choose_color()
      self.display_c()
  def button1(self):
    if self.state == "Start":
      self.state = "Play"
      
  def button2(self):
    if self.state == "Start":
      self.state = "Play"
      
  def button3(self):
    if self.state == "Start":
      self.state = "Play"
      
  def button4(self):
    if self.state == "Start":
      self.state = "Play"
      
  def button5(self):
    if self.state == "Start":
      self.state = "Play"
      
      
button1.when_pressed = game.button1

button2.when_pressed = game.button2

button3.when_pressed = game.button3

button4.when_pressed = game.button4

button5.when_pressed = game.button5
      
      
  
game = Game()
game.start()

try:
  while True:
    time.sleep(0.5)
    
except KeyboardInterrupt:
  game.clean_display()
  print("Bye Bye")