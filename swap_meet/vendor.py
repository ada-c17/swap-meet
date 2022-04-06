class Vendor:
    """
    A class to represent vendors participating in a swap meet. 

    ...

    Attributes
    ----------
    inventory: list
        List of items that a vendor is trading. 

    Methods
    ----------
    add(item):
        Adds an item to inventory.
    remove(item):
        Removes an item from inventory.
    get_by_category(category):
        Makes a list of items that fall within the indicated category.
    swap_items(vendor, my_priority, their_priority):
        Swaps indicated items from inventory of two vendors.
    swap_first_item(vendor):
        Swaps the first item from inventory of two vendors. 
    get_best_category(category):
        Gets item in best condition from indicated category. 
    swap_best_by_category(other, my_priority, their_priority):
        Swaps the best item in a specified category from the invetory of two vendors.

    """
    
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        """Takes in an Item object, adds it to the inventory list, and returns the Item."""
        self.inventory.append(item)
        return item

    def remove(self,item):
        """
        Removes an item from inventory.

            Parameter:
                    item: An Item object
            
            Returns:
                    False if Item is not in inventory. 
                    Item if it is in inventory. 
        """
        if item not in self.inventory:
            return False
        else:
            item_index = self.inventory.index(item)
            return self.inventory.pop(item_index)

    def get_by_category(self, category):
        """ Takes in the category name, returns list of items that fall within indicated category."""
        items_by_category = [item for item in self.inventory if item.category == category]
        return items_by_category
    
    def swap_items(self, vendor, my_item, their_item):
        """
        Swaps indicated items from inventory of two vendors.

            Parameters:
                    vendor: Another instance of Vendor 
                    my_item: Item object that the current instance of Vendor gives
                    their_item: Item object that the current instance of Vendor receives.
            
            Returns:
                    False if Item is not in the inventory of either Vendor object
                    True if swap is successful.
        """
        if not self.remove(my_item):
            return False
        elif not vendor.remove(their_item):
            self.add(my_item)
            return False
        else:
            self.remove(my_item)
            vendor.add(my_item)

            vendor.remove(their_item)
            self.add(their_item)
            return True
    
    def swap_first_item(self, vendor):
        """
        Swaps the first item from inventory of two vendors. 

            Parameter: 
                    vendor: Another instance of Vendor 
            
            Returns:
                    False if vendor inventory is empty. 
                    True if swap is successful. 
        """
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        """
        Gets item in best condition from indicated category. 
            
            Parameter: 
                    category(str): Name of category
            
            Returns:
                    None if there are no items in inventory from indicated category. 
                    Item object with highest condition within inidcated category. 
        """
        items_in_category = self.get_by_category(category)
        if len(items_in_category) == 0:
            return None
        else:
            return max(items_in_category, key = lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Swaps the best item in a specified category from the invetory of two vendors.

            Parameters:
                    other: Another instance of Vendor 
                    my_priority(str): Name of category current instance of Vendor wants to receive 
                    their_priority(str): Name of category other instance of Vendor wants to receive
            Returns:
                    False if there are no items that match the indicated categories. 
                    True if swap is successful. 
        """
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        
        self.swap_items(other, my_best_item, their_best_item)
        return True