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
        Constructs all the necessary attributes for the vender object.
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
        """
        Returns list of items with a given category. 

        If there are no items with the given category, it returns an empty list.

        Parameters
        ----------
        category : str
            string of the category each item must match to be added to the list

        Returns
        -------
        category items list
        """
        category_items = []
        # try:
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items
        # except ValueError:
            # pass
            # return category_items

    def swap_items(self, other_vender, my_item, their_item):
        """
        Returns True if items have been swapped between two inventory lists of two objects. 

        If the vendor's inventory or other vender's invenory is an empty list, returns False.
        If either of the items to be swapped not in appropriate lists, returns False

        Parameters
        ----------
        other_vender: Vender instance object
            The instance of the class Vendor
        my_item: var
            Item instance with given cateogry to be removed from self.inventory and appended to other_vender
        their_item: var
            Item instance with given cateogry to be removed from other_vender.inventory and appended to self.inventory

        Returns
        -------
        True/False
        """
        if my_item not in self.inventory or their_item not in other_vender.inventory:
            return False
        elif not self.inventory or not other_vender.inventory:
            return False
        self.inventory.remove(my_item)
        other_vender.inventory.remove(their_item)

        self.inventory.append(their_item)
        other_vender.inventory.append(my_item)
        return True

    def swap_first_item(self, other_vender):
        """
        Swaps the first item in self.inventory and other_vendor.inventory

        If the vendor's inventory or other vender's invenory is an empty list, returns False.

        Parameters
        ----------
        other_vender: Vender instance object
            The instance of the class Vendor

        Returns
        -------
        True/False
        """
        if not self.inventory or not other_vender.inventory:
            return False

        self.inventory.append(other_vender.inventory.pop(0))
        other_vender.inventory.append(self.inventory.pop(0))
        return True