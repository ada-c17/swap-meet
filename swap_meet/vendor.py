class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory # empty list by default
    
    def add(self, one_item):
        self.inventory.append(one_item)
        return one_item

    def remove(self, one_item):
        try:
            self.inventory.remove(one_item)
            return one_item
        except ValueError:
            return False
        