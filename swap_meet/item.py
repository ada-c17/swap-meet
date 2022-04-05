class Item:
    
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition <= 1:
            return "no comment"
        elif self.condition <= 2:
            return "eh"
        elif self.condition <= 3:
            return "good"
        elif self.condition <= 4:
            return "great"
        elif self.condition <= 5:
            return "perfect, mwah"
