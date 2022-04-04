class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return self.inventory
        

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return self.inventory