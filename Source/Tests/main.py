import random


class color:
    def __init__(self, possible_colors[]):
        self.possibe_colors = possible_colors
        
    def get_random_color(self):
        self.chosen_color = random.choice(self.possibe_colors)
        return self.chosen_color
    
    
class button_handler():
    def __init__(self):
        pass