
class Item:
    category = ""
    
    def __init__(self, category = category, condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        self = "Hello World!"
        return f"{self}"

    def condition_description(self):
        if self.condition <= 1:
            return "Trash"
        if self.condition <= 2:
            return "Bad"
        if self.condition <= 3:
            return "OK"
        if self.condition <= 4:
            return "Good"
        if self.condition <= 5:
            return "Pristine"