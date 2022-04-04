class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    # This method adds the item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # This method removes the matching item from the inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
