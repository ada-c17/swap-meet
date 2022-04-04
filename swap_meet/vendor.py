#from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        # why do we specify that it's a list as a default param?
        if not inventory:
           inventory = []
        self.inventory = inventory

    def add(self, item):
        if not item:
            return False

        self.inventory.append(item)
        return item

    def remove(self, item):
        #inventory_copy = self.inventory.deepcopy
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

