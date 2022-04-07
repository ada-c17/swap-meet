class Item:
    def __init__(self, category=None, condition = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return f"terrible"
        if self.condition == 1:
            return f"not great"
        if self.condition == 2:
            return f"kinda ok"
        if self.condition == 3:
            return f"you'll do"
        if self.condition == 4:
            return f"basic"
        if self.condition == 5:
            return f"vibe"