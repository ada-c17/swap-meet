
class Vendor:
    def __init__(self, inventory= []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            del self.inventory[self.inventory.index(item)]
            return item
        return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
