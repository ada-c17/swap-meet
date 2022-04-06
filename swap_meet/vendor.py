from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return self.inventory[-1]

    def remove(self, item):
        if item not in self.inventory:
            print("Item is not in inventory. Please enter a valid item.")
            return False
        else:
            return self.inventory.pop(self.inventory.index(item))

    def get_by_category(self, category):
        categorized = []

        for item in self.inventory:
            if category == item.category:
                categorized.append(item)

        return categorized
