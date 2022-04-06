class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item): 
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory: 
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items

    
    


