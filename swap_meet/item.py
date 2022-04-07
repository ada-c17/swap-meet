class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_descriptions = {0: "You gotta see it to beleive it",
                                  1: "A hand-me-down many, many times over",
                                  2: "Like revisiting life in your college dorm",
                                  3: "A gift from my ex - he was ok",
                                  4: "Like new - not new but like it",
                                  5: "The Beyonce of objects"}

        return condition_descriptions[self.condition]
