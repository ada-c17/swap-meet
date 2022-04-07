class Vendor:
    """
    A class to represent a Vendor.
    
    '''
    Attributes
    ----------
    inventory (list): List of items, default is a empty list.

    Methods
    -------
    add(item):
        Adds an item to the inventory.

    remove(item):
        Removes an item from the inventory.
        
    get_by_category(category):
        Returns a list of items with same category as argument.
        
    swap_items(other_vendor, my_item, their_item)
        Swaps specific item (my_item) with another vendor's item (their_item).

    swap_first_item(other_vendor)
        Swaps the first item in inventory between this vendor and another vendor.

    get_best_by_category(category)
        Returns the item with the highest condition value in that specific category.

    swap_best_by_category(other, my_priority, their_priority)
        Swaps the items with the highest condition value in the 
        preferred category with another vendor.
    """

    def __init__(self, inventory=None):
        """
        Constructs all the necessary attributes for the Vendor object.

        Parameters
        ----------
        inventory (list, optional): List of items, default is a empty list.
        """

        self.inventory = inventory if inventory else []


    def add(self, item):
        """
        Adds an item to the inventory.
        
        Parameters
        ----------
        item (str): an item to add

        Returns
        -------
        item
        """

        self.inventory.append(item)
        return item


    def remove(self, item):
        """
        Removes an item from the inventory.
        
        Parameters
        ----------
        item(str): an item to remove

        Returns
        -------
        Returns item if successful, False otherwise.
        """

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False


    def get_by_category(self, category):
        """
        Returns a list of items with same category as argument.
        
        Parameters
        ----------
        category(str): category of an inventory item
        
        Returns
        -------
        list
        """

        items_with__same_category_list = []
        for item in self.inventory:
            if category in item.category:
                items_with__same_category_list.append(item) 
        return items_with__same_category_list


    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swaps specific item (my_item) with another vendor's item (their_item).
        
        Parameters
        ----------
        other_vendor(object): the other vendor that this vendor is trading with
        my_item(object): an object in this vendor's inventory
        their_item(object): an object in the other vendor's inventory
        
        Returns
        -------
        Returns True if the trade successful, False otherwise
        """
        if not my_item in self.inventory or not their_item in other_vendor.inventory:
            return False
        
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)

        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        return True

    
    def swap_first_item(self, other_vendor):        
        """
        Swaps the first item in each inventory between this vendor and the other vendor.
        
        Parameters
        ----------
        other_vendor(object): the other vendor that this vendor is trading with
        
        Returns
        -------
        Returns True if the trade was successful, False otherwise
        """
        
        if not self.inventory or not other_vendor.inventory:
            return False
            
        self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
        return True

    
    def get_best_by_category(self, category):
        """
        Returns the item with the highest condition value in that specific category.
        
        Parameters
        ----------
        category(str): category of an inventory item
        
        Returns
        -------
        Returns the item with highest condition value if successful, None otherwise
        """

        get_by_category_list = self.get_by_category(category)

        if not get_by_category_list:
            return None

        best_item = get_by_category_list[0]
        for item in get_by_category_list:
            if item.condition > best_item.condition:
                best_item = item
        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps the items with the highest condition value in the 
        preferred category with another vendor.
        
        Parameters
        ----------
        other_vendor(object): the other vendor that this vendor is trading with
        my_priority(str): a category requested by this vendor
        their_priority(str): a category requested by the other vendor
        
        Returns
        -------
        Returns True if trade was successful, False otherwise
        """

        my_item = self.get_best_by_category(their_priority)
        other_item = other.get_best_by_category(my_priority)

        if not my_item or not other_item:
            return False
        self.swap_items(other,my_item,other_item)
        return True