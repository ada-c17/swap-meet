class Item:
    def __init__(self, category = None, condition = 0, age = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
        self.age = age
        

    def __str__(self):
        return "Hello World!"


    def age_statement(self):
        return f"This item was made {self.age} months ago."
    

    def condition_description(self):
        if self.condition == 0:
            description = "horrendous quality"
        elif self.condition == 1:
            description = "terrible quality"
        elif self.condition == 2:
            description = "bad quality"
        elif self.condition == 3:
            description = "decent quality"
        elif self.condition == 4:
            description = "great quality"
        elif self.condition == 5:
            description = "exquisite quality"
        return f"This item's condition is {description}"