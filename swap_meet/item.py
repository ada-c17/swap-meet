class Item:
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return("Hello World!")

    def __repr__(self): #created repr dunder method just for funzies
        rep = f"Item({self.category}, {str(self.condition)}, {str(self.age)})"
        return rep

    def condition_description(self):
        if self.condition < 1:
            custom_message =  "good as garbage"
        elif 1 <= self.condition < 2:
            custom_message = "heavily used"
        elif 2 <= self.condition < 3:
            custom_message = "moderately used"
        elif 3 <= self.condition < 4:
            custom_message = "lightly used"
        elif 4 <= self.condition < 5:
            custom_message = "like new"
        elif self.condition == 5:
            custom_message = "new"
        return f"This item is {custom_message}."
