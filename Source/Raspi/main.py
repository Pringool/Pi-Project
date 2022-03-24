from colors import Colors
from disp import Display
from gpiozero import LED, Button as button
import time
import random

  
  
class Game:
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
  timer = 5
  def __init__(self):
    self.disp = Display()
    self.c = Colors()
    self.level = 0
    self.state = "Start"
    self.posi = ["mid", "ltop", "rtop", "lbot", "rbot", "left", "right"]
    
  def display_c(self, pos = "mid"):
    self.disp.display_color(self.c.get_color(), pos)
    
  def clean_display(self):
    self.disp.clear()
    
  def clean_led(self):
    self.red.off()
    self.blue.off()
    self.green.off()
    self.white.off()
    self.yellow.off()
    
    
  def start(self):
    self.clean_display()
    self.round_system()
    self.disp.display_start()
    
  def win(self):
    self.disp.win_screen()  
    
  def check_right(self, button_pressed):
    if button_pressed == "1":
      if self.c.get_color() == "WHITE":
        print("correct!")
        self.level += 1
        self.round_system()
        Game.white.off()
      else:
        print("Wrong!")
        self.clean_led()
        self.round_system()
        
    elif button_pressed == "2":
      if self.c.get_color() == "GREEN":
        print("correct!")
        self.level += 1
        self.round_system()
        Game.green.off()
      else:
        print("Wrong!")
        self.clean_led()
        self.round_system()
        
    elif button_pressed == "3":
      if self.c.get_color() == "BLUE":
        print("correct!")
        self.level += 1
        self.round_system()
        Game.blue.off()
      else:
        print("Wrong!")
        self.clean_led()
        self.round_system()
        
    elif button_pressed == "4":
      if self.c.get_color() == "YELLOW":
        print("correct!")
        self.level += 1
        self.round_system()
        Game.yellow.off()
      else:
        print("Wrong!")
        self.clean_led()
        self.round_system()
        
    elif button_pressed == "5":
      if self.c.get_color() == "RED":
        print("correct!")
        self.level += 1
        self.round_system()
        Game.red.off()
      else:
        print("Wrong!")
        self.clean_led()
        self.round_system()
        
        
  def round_system(self):
    self.clean_display()
    print(self.level)
    if self.state == "Play":
      if self.level >= 0 and self.level < 5:
        self.c.choose_color()
        self.display_c()
      elif self.level >= 5 and self.level <= 9:
        self.start_t = time.time()
        self.c.choose_color()
        Game.timer -= 0.2
        print(Game.timer)
        self.display_c()
      elif self.level >= 10 and self.level <= 15:
        self.start_t = time.time()
        self.c.choose_color()
        Game.timer -= 0.3
        print(Game.timer)
        self.display_c(random.choice(self.posi))
      elif self.level >= 16:
        self.win()
      
      
  def button1_p(self):
    if self.state == "Start":
      self.state = "Play"
      self.round_system()
    else: 
      Game.white.on()
      self.check_right("1")
      
  def button2_p(self):
    if self.state == "Start":
      self.state = "Play"
      self.round_system()
    else: 
      Game.green.on()
      self.check_right("2")
      
  def button3_p(self):
    if self.state == "Start":
      self.state = "Play"
      self.round_system()
    else: 
      Game.blue.on()
      self.check_right("3")
      
  def button4_p(self):
    if self.state == "Start":
      self.state = "Play"
      self.round_system()
    else: 
      Game.yellow.on()
      self.check_right("4")
      
  def button5_p(self):
    if self.state == "Start":
      self.state = "Play"
      self.round_system()
    else: 
      Game.red.on()
      self.check_right("5")
      
game = Game()
game.start()      

game.button1.when_pressed = game.button1_p

game.button2.when_pressed = game.button2_p

game.button3.when_pressed = game.button3_p

game.button4.when_pressed = game.button4_p

game.button5.when_pressed = game.button5_p



try:
  while True:
    time.sleep(0.5)
    if game.level > 5 and not game.level >= 16:
      if time.time() >= game.start_t + game.timer:
        print(":|")
        game.clean_display()
    
except KeyboardInterrupt:
  game.clean_display()
  game.clean_led()
  print("\nBye Bye\n")
