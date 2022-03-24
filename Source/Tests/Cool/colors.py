import random


class Colors:
  def __init__(self):
    self._color = ["green","blue","white"]#,"red","yellow"]
    
  def get_color(self):
    return self.color.upper()
    
  def choose_color(self):
    self.color = random.choice(self._color)

