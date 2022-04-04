class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        try:
            item_index = self.inventory.index(item)
            return self.inventory.pop(item_index)
        except ValueError:
            return False
