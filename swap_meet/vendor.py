class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
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
        bool: True if item is inventory, False otherwise.
        """

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, specific_category):
        """
        Adds the items in the instance's inventory that are of a specific category.

        Parameters: 
        specific_category (str): A category.

        Returns:
        category_matches (list): Items in the inventory matching the category.
        """

        category_matches = []
        for item in self.inventory:
            if item.category == specific_category:
                category_matches.append(item)
        return category_matches

    def swap_items(self, friend, my_item, their_item):
        """
        Swaps items in vendor's inventory and friend's inventory.

        Parameters: 
        friend (class): Vendor instance of friend.
        my_item (str): Category the vendor wants to receive.
        their_item (str): Category friends wants to receive.

        Returns:
        (bool): True if swapping occurs, False if not.
        """

        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        '''
        Removes first item from a vendor's inventory and a friend's inventory.

        Parameter:
        friend (class): An instance of another Vendor.

        Returns: 
        (bool): True is first items the Vendor and the friend swap items, False otherwise.
        '''
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])

            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        return False
    
    def get_best_by_category(self, specific_category):
        '''
        Returns the item with the best condition in a specific category.

        Parameters:
        specific_category (str): Category.

        Returns: 
        (instance or bool): Returns instance of an item in a specfic category's best condition or None if not found.
        '''
        best_by_category = None
        highest_condition = 0
        
        for item in self.inventory:
            if item.category == specific_category and item.condition > highest_condition:
                    best_by_category = item
                    highest_condition = item.condition
        return best_by_category
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Determines if vendor's item priority and other's item priority exists and swaps items.

        Parameters: 
        other (class): The other Vendor instance.
        my_priority (str): The category that the Vendor wants to receive.
        their_priority (str): The category that the other party wants to receive.

        Returns: 
        (bool): True if items are swapped, False is not.
        '''
        
        their_best_item = self.get_best_by_category(their_priority)
        my_best_item = other.get_best_by_category(my_priority)

        if not their_best_item or not my_best_item:
            return False
        
        swapped_items = self.swap_items(other, their_best_item, my_best_item)
        return swapped_items