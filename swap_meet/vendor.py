from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return self.inventory[-1]

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            return self.inventory.pop(self.inventory.index(item))

    def get_by_category(self):
        pass
