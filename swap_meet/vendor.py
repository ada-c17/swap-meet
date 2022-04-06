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
        All instances of Vendor will have this method swap_items:
        - takes 3 arguments; another Vendor, my_item, their_item
        - removes my_item from this Vendor's inventory
        - removes their_item from the other Vendor's inventory
        - returns True if both inventories have the respective items
        - returns False if one of the items is not contained in respective inventories
        """

        if my_item in self.inventory and their_item in swap_vendor.inventory:
            self.inventory.remove(my_item)
            swap_vendor.inventory.append(my_item)
            self.inventory.append(their_item)
            swap_vendor.inventory.remove(their_item)
            return True
        return False

    def swap_first_item(self, swap_vendor):
        """
        All instances of Vendor will have this method swap_first_items:
        - takes one argument; another Vendor
        - method considers the first item in the instance's inventory, and the first item in the friend's inventory
        - removes the first item from its inventory, and adds the friend's first item
        - removes the first item from the friend's inventory, and adds the instances first item
        - returns True
        - either itself or the friend have an empty inventory, the method returns False
        """
        while len(self.inventory) >= 1 and len(swap_vendor.inventory) >= 1:
            self_first_item = self.inventory[0]
            swap_vendor_first_item = swap_vendor.inventory[0]

            self.inventory[0] = swap_vendor_first_item
            swap_vendor.inventory[0] = self_first_item
            return True
        return False