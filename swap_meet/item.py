class Item:
    def __init__(self, category='', condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"
        
    def condition_description(self):
        descriptions = { 
            0: "I should be paying you to take it off my hands.",
            1: "Just don't touch your face after handling.",
            2: "No refunds.",
            3: "Not too shabby.",
            4: "Looking good!",
            5: "Absolutely immaculate. Exquisitely rare find!"
        }
        
        self.condition = int(self.condition)

        return descriptions[self.condition]
