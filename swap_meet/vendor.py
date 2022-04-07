from swap_meet.item import Item

class Vendor:
    """
    A class to hold vendor object data.

    ...
    Attributes
    ----------
    inventory: list
        items in inventory

    Methods
    -------
    add(item)
        Adds an item to inventory.
    remove(item)
        Removes an item from inventory.
    get_by_category(category)
        Get all items in inventory that fall under a specified category.
    """

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        """
        Adds an item to inventory.

        Parameters
        ----------
            item: str
                item to be added to inventory
        Returns
        -------
        Item added to inventory.
        """
        self.inventory.append(item)
        return self.inventory[-1]

    def remove(self, item):
        """
        Removes an item from inventory.

        Parameters
        ----------
            item: str
                item to be removed from inventory
        Returns
        -------
        Item removed from inventory. If item does not exist in inventory, return False.
        """
        if item not in self.inventory:
            print("Item is not in inventory. Please enter a valid item.")
            return False
        else:
            return self.inventory.pop(self.inventory.index(item))

    def get_by_category(self, category):
        """
        Get all items in inventory that fall under a specified category.

        Parameters
        ----------
            category: str
                specified category to filter items in inventory
        Returns
        -------
        List of items in inventory that falls under specificed category.
        """
        categorized = []

        for item in self.inventory:
            if category == item.category:
                categorized.append(item)

        return categorized

    def swap_items(self, vendor, my_item, their_item):
        """
        Swaps an item from a vendor (self) to an item from a friend (vendor).

        Parameters
        ----------
            vendor: instance of Vendor
                friend that vendor is swapping with
            my_item: instance of Item
                item vendor intends to swap
            their_item: instance of Item
                item friend intends to swap
        Returns
        -------
        True if items are swapped, False if items cannot be swapped.
        """
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.add(their_item)
            self.remove(my_item)
            vendor.add(my_item)
            vendor.remove(their_item)
            return True
