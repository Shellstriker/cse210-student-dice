import random


# TODO: Define the Thrower class here.
class thrower(dice, num_throws):    
    def __init__(self):
        self.dice = []
        self.num_throws = 0
        
    def can_throw(self):
        return (self.dice.count(5) > 0 or self.dice.count(1) > 0 or self.num_throws == 0)
    
    def get_points(self):
        return self.dice.count(5)*50 + self.dice.count(1)*100

    def throw_dice():
        self.dice.clear()
        for i in range(5):
            result = random.randint(1,6)
            self.dice.append(result)
        self.num_throws += 1