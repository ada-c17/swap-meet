from .item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            print("Item not found.")
            return False
        return item

    def get_by_category(self, category):
        # Initialize empty list that will hold all items of the correct category
        relevant_items = []
        # Iterate through inventory; if item is of correct category, add to list
        for item in self.inventory:
            if item.category == category:
                relevant_items.append(item)
        return relevant_items

