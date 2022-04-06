class Decor:
    def __init__(self, category="Decor", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        if self.condition < 2:
            return "Quite used but super cute and could refactor it like bad code"
        elif 2 <= self.condition <= 3:
            return "Very used but quality fabric and fit"
        elif 3 <= self.condition <= 4:
            return "Very used but quality fabric and fit"
        elif 4 <= self.condition <= 4.5:
            return "Mint condition, sparkly and all"
        elif 4.5 <= self.condition <= 4.9:
            return "Label still on, never worn, like new"
        elif self.condition == 5:
            return "Label still on, never worn, like new"




