class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        rounded_number = round(self.condition)
        if rounded_number == 0:
            return "Heavily used!"
        elif rounded_number == 1:
            return "Moderately used!"
        elif rounded_number == 2:
            return "Slightly used!"
        elif rounded_number == 3:
            return "Used but well maintained!"
        elif rounded_number == 4:
            return "Just like brand new!"
        elif rounded_number == 5:
            return "Brand new!"