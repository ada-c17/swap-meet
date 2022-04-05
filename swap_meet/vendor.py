# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        category_items =[]
        for item in self.inventory:
            if category == item.category:
                category_items.append(item)
        return category_items
