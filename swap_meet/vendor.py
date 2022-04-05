# Wave 1
from curses import beep
from nis import cat
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


class Vendor:
    """
    attributes: inventory
    methods: 
        - In wave 1: add() and remove()
        - In wave 2: get_by_category(), 
        - In Wave 3: swap_items()
        - In Wave 4: swap_first_item()
        - In Wave 6: get_best_by_category()
    """

    # Wave 1
    def __init__(self, inventory = None):
        """Inventory is keyword argument that optionally pass in."""
        # assign empty list to inventory when the if statement is falsy. 
        # Otherwise, assign inventory as value of object's inventory.
        if not inventory:
            inventory = []
        self.inventory = inventory
        
        
    def add(self, item):
        """Adding new item into inventory and returns the added item."""
        self.inventory.append(item)
        return item


    def remove(self, item):
        """Removing item from inventory if it is matching the paramenter item and returns the removed item."""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    # Wave 2
    def get_by_category(self, category):
        """
        - Adding item object into a list if category is in vendor's inventory
        - Return empty list if inventory list is empty. Otherwise returns list of items in inventory.

        """
        items_list = []
        if len(self.inventory) > 0:
            # loop over inventory list to check each item object's category
            # add item object into list if its category macthes to parameter
            for item in self.inventory:
                if item.category == category:
                    items_list.append(item)
            return items_list
        return []


    # Wave 3
    def swap_items(self, vendor, my_item, their_item):
        """
        If my item is in my inventory and their item is in friend's inventory:
            - remove my item from my inventory and add it to friend's inventory
            - remove their item from friend's inventory and add it to my inventory
            - return True
        Otherwise return False
        """
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            return True
        return False
            

    # Wave 4
    def swap_first_item(self, vendor):
        """
        Swapping first item of my inventory and friend's inventory:
        - if both inventories are not empty then return True
        - otherwise, return False
        """
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]
            return True
        return False


    # Wave 6
    def get_best_by_category(self, category):
        """
        - Returning best item if inventory for item is not empty and has the highest condition and matching category
        - Otherwise, return None
        """

        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.category == category:  
                    max_condi = max([item.condition for item in self.inventory if item.category == category])
                    if item.condition == max_condi:
                        return item
        return None






        