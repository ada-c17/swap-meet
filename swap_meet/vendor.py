class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, discarded_item):
        if discarded_item not in self.inventory:
            return False
        else: 
            self.inventory.remove(discarded_item)
            return discarded_item