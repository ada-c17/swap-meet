class Vendor:
    # wave 1
    # attributes: 
    #   inventory - an empty list
    # instance methods:
    #   add - takes in one item and adds to inventory, returns item added
    #   remove - takes in one item and removes from inventory, returns item removed

    # wave 2
    # add instance method:
    #   get_by_category - takes in one string item and returns list of inventory items in the same category

    def __init__(self, inventory=[]):
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
        same_category_items = []
        for item in self.inventory:
            if item.category == category:
                same_category_items.append(item)
        return same_category_items