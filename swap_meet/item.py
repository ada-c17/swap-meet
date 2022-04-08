from swap_meet.vendor import Vendor
class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"
    
    def age_statement(self):
        return f"This item was created {self.age} months ago."
    
    def condition_description(self):
        CONDITIONS ={
            0 : "Perfect!",
            1 : "Really good!",
            2 : "Pretty nice!",
            3:  "It's in decent shape!",
            4 : "Watch out!",
            5:  "Oh no! It's no good!"
        }
        return CONDITIONS[self.condition]
        