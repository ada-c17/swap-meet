class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 3:
            return "Quite used but super cute and could refactor it like bad code"
        # elif 1 <= self.condition < 2:
        #     return "Not bad, not bad at all"
        # elif 1 <= self.condition < 2:
        #    return "Very used but quality fabric and fit"
        # elif 3 <= self.condition < 4:
        #     return "Passable"
        elif 3 <= self.condition < 5:
            return "Mint condition, sparkly and all"
        elif self.condition == 5:
            return "Nevern worn, labels and all, not like new -- it IS new!"
