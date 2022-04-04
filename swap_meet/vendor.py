class Vendor:
     """
    A class to represent a vendor.

    ...

    Attributes
    ----------
    inventory : list
        list of strings representing items in inventory

    Methods
    -------
    add(item):
        Adds an item to the inventory list.
        Returns item.
    
    remove(item):
        Removes an item from the inventory list.
        Returns item.
        If item not in list, returns False.
    """


    def __init__(self, inventory = None): #do not set keyword argument to list bc it is a mutable type
        """
        Constructs all the necessary attributes for the vendor object.

        Parameters
        ----------
            inventory : list
                list of strings representing items in inventory
        """

        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        """
        Appends the item to the inventory list.

        Parameters
        ----------
        item : str

        Returns
        -------
        item
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        Removes item from inventory list.

        If the item is not in list, then the list is not changed and return is None.

        Parameters
        ----------
        item : str

        Returns
        -------
        item or None
        """
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
