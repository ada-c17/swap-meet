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

    get_by_category(category):
        Creates list of items whose category attribute matches the input category.
        Returns list. 

    swap_items(vendor_to_swap_with, item_vendor_swaps, item_vendor_gets):
        Removes item_vendor_swaps from vendor.inventory list and appends item_vendor_gets to list.
        Removes item_vendor_gets from vendor_to_swap_with.inventory list and appends.item_vendor_swaps to list
        Returns vendor's list.

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
    
    def get_by_category(self, category):
        """
        Creates a list of items from inventory whose category attributes match the input category. 

        If no items from inventory are of the category passed as an argument, returns empty list.

        Parameters
        ----------
        category : str

        Returns
        -------
        items: list
        """
        # items = []
        # for item in self.inventory:
        #     if item.category == category:
        #         items.append(item)
        # return items

        return [item for item in self.inventory if item.category == category]
    
    def swap_items(self, vendor, my_item, vendor_item):
        """
        Removes and appends 2nd and 3rd parameters from my inventory respectively.

        Appends and removes 2nd and 3rd parameters from vendor's inventory respectively.

        Parameters
        -------
        vendor: composite object
        my item: component object 
        vendor_item: component object

        Returns
        -------
        self.inventory: object
        
        """
        if my_item in self.inventory and vendor_item in vendor.inventory:
            self.inventory.remove(my_item) 
            self.inventory.append(vendor_item)            
            vendor.inventory.remove(vendor_item)       
            vendor.inventory.append(my_item) 

            return self.inventory
        else:
            return None
        # try:
        #     item_vendor_swaps in self.inventory and item_vendor_gets in vendor_to_swap_with.inventory
        # except ValueError:
        #     return None
        # finally:
        #     self.inventory.remove(item_vendor_swaps) 
            
        #     vendor_to_swap_with.inventory.remove(item_vendor_gets)            
        #     self.inventory.append(item_vendor_gets)
        
        #     vendor_to_swap_with.inventory.append(item_vendor_swaps)
            
        #     return self.inventory

    def swap_first_item(self, vendor):
        """
        Removes and appends first item from vendor and first item vendor_to_swap_with from my inventory respectively.

        Removes and appends first item from vendor_to_swap_with and first item vendor from vendor's inventory respectively.

        Parameters
        -------
        vendor: object

        Returns
        -------
        boolean
        """
        try:
            self.inventory[0], vendor.inventory[0] = vendor.inventory[0], self.inventory[0]

            return True
        except IndexError:
            return False



