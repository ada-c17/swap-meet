class Vendor:
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        for items in self.inventory:
            if item == items:
                self.inventory.remove(items)
                return items
        return False