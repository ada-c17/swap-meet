from .item import Item

class Vendor:
    """
    A class to represent a vendor.

    Attributes
    ----------
    inventory : list
        list of items in inventory
        optional attribute defaulted aas None 
        Uses logic to create empty dictionary if needed

    Methods
    -------
    add(item):
        appends new item to inventory list
    remove(item):
        removes item from inventory list
        if item not in list, raises ValueError and returns False
    """

    def __init__(self, inventory = None):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
            inventory : list
                list of vendor items
        """
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """Takes in an item and appends to inventory list."""
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes specific item from inventory list if available, if not, returns False."""
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        category_items = []
        # try:
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items
        # except ValueError:
            # pass
            # return category_items