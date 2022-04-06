class Item:
    def __init__(self, category = "", condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        description = { 0: "xoxo let it go",
                        1: "florals? for spring?",
                        2: "moderately fetch",
                        3: "bend and snap",
                        4: "star dazzle award",
                        5: "what dreams are made of"
        }
        return description[self.condition]
