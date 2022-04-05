from .item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        # OLD IMPLEMENTATION
        # try:
        #     self.inventory.remove(item)
        # except ValueError:
        #     print("Item not found.")
        #     return False
        # return item

    def get_by_category(self, category):
        # Initialize empty list that will hold all items of the correct category
        relevant_items = []
        # Iterate through inventory; if item is of correct category, add to list
        for item in self.inventory:
            if item.category == category:
                relevant_items.append(item)
        return relevant_items

    def swap_items(self, other_vendor, selfs_item, others_item):
        print(f"My inventory has {len(self.inventory)} items in it. Other's inventory has {len(other_vendor.inventory)} items in it.")
        #remove self's item from self's inventory
        self.remove(selfs_item)
        #add self's item to other's inventory
        other_vendor.inventory.append(selfs_item)
        #remove other's item from other's inventory
        other_vendor.remove(others_item)
        #add other's item to self's inventory
        self.inventory.append(others_item)
        print(f"My inventory now has {len(self.inventory)} items in it. Other's inventory now has {len(other_vendor.inventory)} items in it.")
        return True

