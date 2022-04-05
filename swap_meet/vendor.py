# Wave 1
from nis import cat
from swap_meet.item import Item


class Vendor:
    """
    attributes: inventory
    methods : add and remove
    """

    def __init__(self, inventory = None):
        """Inventory is keyword argument that optionally pass in."""
        # assign empty list to inventory when the if statement is falsy. 
        # Otherwise, assign inventory as value of object's inventory.
        if not inventory:
            inventory = []
        self.inventory = inventory
        # self.obj_item = Item()

        
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
        