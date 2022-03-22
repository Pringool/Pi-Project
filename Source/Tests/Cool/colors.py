import random


class Colors:
  def __init__(self):
    self._color = ["Grün","Blau","Weiß","Rot","Gelb"]
    
  def get_color(self):
    return self.color
    
  def choose_color(self):
    self.color = random.choice(self._color)

