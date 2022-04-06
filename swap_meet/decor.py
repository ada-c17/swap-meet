class Decor:
    def __init__(self, category="Decor", condition=None):
        self.category = category
        if not condition:
            condition = 0
        self.condition = condition
    
    def __str__(self):
        return "Something to decorate your space."