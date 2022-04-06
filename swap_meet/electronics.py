class Electronics:
    def __init__(self, category="Electronics", condition=None):
        self.category = category
        if not condition:
            condition = 0
        self.condition = condition
    
    def __str__(self):
        return "A gadget full of buttons and secrets."
