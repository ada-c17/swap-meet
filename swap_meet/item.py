class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if 0 < self.condition <= 1:
            return "Falling Apart"
        elif 1 < self.condition <= 2:
            return "Heavily Used"
        elif 2 < self.condition <= 3:
            return "Fair"
        elif 3 < self.condition <= 4:
            return "Good"
        elif 4 < self.condition <= 5:
            return "Like New"