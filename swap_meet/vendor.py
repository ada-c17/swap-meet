class Vendor:
    # wave 1
    # attributes: 
    #   inventory - an empty list
    # instance methods:
    #   add - takes in one item and adds to inventory, returns item added
    #   remove - takes in one item and removes from inventory, returns item removed

    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        self.inventory.remove(item)
        return item