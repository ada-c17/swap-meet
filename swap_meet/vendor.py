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

    def swap_items(self, swap_vendor, my_item, their_item):

        """
        Instances of Vendor will have this method swap_items:
        * takes 3 arguments; another Vendor, my_item, their_item
        * removes my_item from this Vendor's inventory
        * removes their_item from the other Vendor's inventory
        * returns True if both inventories have the respective items
        * returns False if one of the items is not contained in respective inventories
        """

        if my_item in self.inventory and their_item in swap_vendor.inventory:
            self.inventory.remove(my_item)
            swap_vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            swap_vendor.inventory.remove(their_item)
            return True
        return False
