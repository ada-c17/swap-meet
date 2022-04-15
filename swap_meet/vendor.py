class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if not inventory else inventory
    
    def add(self, item):
        """Adds an item to the instance's inventory and returns it."""
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        Removes items from the instance's inventory.

        Parameter: 
        item (str): Inventory item to be removed.

        Returns:
        Instance or bool: False if item is not in inventory, returns item 
        otherwise.
        """

        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, specific_category):
        """
        Collects the items in the instance's inventory that are of a specific 
        category.

        Parameters: 
        specific_category (str): A category.

        Returns:
        category_matches (list): Items in the inventory matching the category.
        """

        return [item for item in self.inventory 
        if item.category == specific_category]

    def swap_items(self, friend, my_item, their_item):
        """
        Swaps items in vendor's inventory and friend's inventory.

        Parameters: 
        friend (class): Vendor instance of friend.
        my_item (str): Category the vendor wants to receive.
        their_item (str): Category friends wants to receive.

        Returns:
        (bool): False if swapping does not occurs, True otherwise.
        """

        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        
        friend.inventory.append(my_item)
        self.inventory.remove(my_item)
            
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)
        return True
    
    def swap_first_item(self, friend):
        '''
        Swaps the first item from a vendor's inventory and a friend's inventory.

        Parameter:
        friend (class): An instance of another Vendor.

        Returns: 
        (bool): False if an item does not exist in the Vendor 
        or the friend's inventory, 
        True otherwise.
        '''
        if not self.inventory or not friend.inventory:
            return False
        
        self.inventory[0], friend.inventory[0] = friend.inventory[0], self.inventory[0]
        return True
    
    def get_best_by_category(self, specific_category):
        '''
        Returns the item with the best condition in a specific category.

        Parameters:
        specific_category (str): Represents a category.

        Returns: 
        (instance or bool): Returns the vendor's instance of an item 
        in a specfic category's best condition or None if not found.
        '''
        best_by_category = None
        highest_condition = 0
        
        for item in self.inventory:
            if (item.category == specific_category and 
                item.condition > highest_condition):
                    best_by_category = item
                    highest_condition = item.condition

        return best_by_category
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Determines if vendor's item priority and other's item 
        priority exists and swaps items.

        Parameters: 
        other (class): The other Vendor instance.
        my_priority (str): The category that the Vendor wants to receive.
        their_priority (str): The category that the other party wants to 
        receive.

        Returns: 
        (bool): True if items are swapped, False is not.
        '''
        
        their_best_item = self.get_best_by_category(their_priority)
        my_best_item = other.get_best_by_category(my_priority)

        if not their_best_item or not my_best_item:
            return False
        
        return self.swap_items(other, their_best_item, my_best_item)