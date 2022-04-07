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
    swap_items(vendor, my_item, their_item)
        Swaps a specified item from a vendor (self) for a specified item from a
        friend (vendor).
    swap_first_item(vendor)
        Swaps first item from a vendor (self) for first item from a friend (vendor).
    get_best_by_category(specified_category)
        Finds the highest condition item in inventory that matches specified
        category.
    swap_best_by_category(other, my_priority, their_priority)
        Swaps items between self and other if item of other's prioritized category
        exists in self's inventory and item of self's prioritized category is in
        other's inventory.
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
        Swaps a specified item from a vendor (self) for a specified item from a
        friend (vendor).

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

    def swap_first_item(self, vendor):
        """
        Swaps first item from a vendor (self) for first item from a friend (vendor).

        Parameters
        ----------
            vendor: instance of Vendor
                friend that vendor is swapping with
        Returns
        -------
        True if items are swapped, False if items cannot be swapped.
        """
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, their_item)
            return True

    def get_best_by_category(self, specified_category):
        """
        Finds the highest condition item in inventory that matches specified
        category.

        Parameters
        ----------
            specified_category: str
                category to filter conditions of items
        Returns
        -------
        Item with the highest condition in specified category.
        """
        if len(self.inventory) == 0:
            return None

        best_item = self.inventory[0]

        for item in self.inventory:
            if item.category == specified_category and item.condition > \
                best_item.condition:
                best_item = item

        if best_item.category != specified_category:
            return None

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps items between self and other if item of other's prioritized category
        exists in self's inventory and item of self's prioritized category is in
        other's inventory.

        Parameters
        ----------
            other: instance of Vendor
                vendor trading with
            my_priority: str
                category first vendor wants
            their_priority: str
                category other vendor wants
        Returns
        -------
        True if items are swapped and False if items are not swapped.
        """
        if other.get_best_by_category(my_priority) and \
            self.get_best_by_category(their_priority):
            self.swap_items(other, self.get_best_by_category(their_priority), \
                other.get_best_by_category(my_priority))
            return True
        else:
            return False
