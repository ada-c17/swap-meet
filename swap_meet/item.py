from swap_meet.vendor import Vendor
class Item:
    def __init__(self, category='', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return 'Hello World!'
    
    def condition_description(self):
        value = round(self.condition)
        if value == 5:
            return "Straight outta da display"
        if value == 4:
            return "Basically new"
        if value == 3:
            return "Yah it's used, but we here to be sustainableee"
        if value == 2:
            return "It ain't THAT bad... maybe just a litte"
        if value == 1:
            return "It's intact"
        if value == 0:
            return "Just TAKE it!"        
