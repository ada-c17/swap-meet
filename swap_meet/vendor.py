from unicodedata import category
from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category_str):
        category_items = []
        for item in self.inventory:
            if item.category == category_str:
                category_items.append(item)
        return category_items
