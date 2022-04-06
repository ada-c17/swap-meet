class Item:
    def __init__(self, category = "", condition =0):
        self.category = category
        self.condition = float(condition)
    
    def __str__(self):
        return "Hello World!"

    def condition_description (self):
        if 4 < self.condition <= 5:
            description = "Best thing I've ever seen"
        elif 3 < self.condition <= 4:
            description = "I liked it but I don't love it"
        elif 2 < self.condition <= 3:
            description = "Fair"
        elif 1 < self.condition <= 2:
            description = "Meh"
        elif 0 < self.condition <= 1:
            description = "Not recommended"
        else: 
            description = "Don't you dare"
        return description 