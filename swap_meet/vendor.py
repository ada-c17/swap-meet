class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        

    def get_by_category (self, category):   
        same_category = []
        for item in self.inventory:
            if category == item.category:
                same_category.append(item)
            
        return same_category


