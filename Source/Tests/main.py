import random


class color():
    def __init__(self, possible_colors=[]):
        self.possibe_colors = possible_colors
        
    def get_random_color(self):
        self.chosen_color = random.choice(self.possibe_colors)
        return self.chosen_color
    
    
class button_handler():
    def __init__(self, amount_buttons):
        self.amount_buttons = amount_buttons
        self.buttons = []

        for i in range(self.amount_buttons):
            self.buttons.append(i)

    
    def check_color(self):
        self.right_button_color = c.get_random_color()
    
        
        
class rounds():
    def __init__(self, max_round_amount):
        self.max_rounds = max_round_amount
        
    def start_round(self):
        pass
    def next_round(self):
        pass
    def game_over(self):
        pass
        
c = color(["White", "Brown", "Yellow", "Blue", "Green", "Red"])
for i in range(0,10):
    print(c.get_random_color())

b = button_handler(6)
print(b.buttons)




