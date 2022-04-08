class Vendor:
    '''
    A class for a Vendor at a swap-meet who has items. The Vendor may want to 
        trade with other vendors based on item category, condition, or both.
    '''

    def __init__(self, inventory=None):
        '''
        Parameter: inventory (list): optional list of vendor inventory. 
        None if not defined, w/attribute set to an empty string. 
        Otherwise set to input parameter.
        '''

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        '''
        Adds an item to a vendor's inventory
        Parameter: item (string, or class object): represents a swappable item
        Returns: the added item
        '''

        self.inventory.append(item)
        return item

    def remove(self, item):
        '''
        Removes an item from a vendor's inventory
        Parameter: item (string, or class object): represents a swappable item
        Returns: the removed item if removed, otherwise False
        '''

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        '''
        Gets a list of every item a vendor has that is in a certain category
        Parameter: category (string): represents the category of a swappable item
        Returns: a list of items with the correct desired category
        '''

        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, other_vendor, self_item, their_item):
        '''
        Facilitates a swap between two vendors for two given items, and updates
            each vendor's inventory list accordingly.
        Parameters: 
            other_vendor (another Vendor instance): vendor to swap with
            self_item (string): an item in the Vendor's own inventory
            their_item (string): an item in the other Vendor's inventory
        Returns: True if the swap was completed, otherwise False
        '''

        if self_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(self_item)
            other_vendor.add(self_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        '''
        Facilitates a swap of the first inventory item for two vendors
            and updates each vendor's inventory list accordingly.
        Parameter: other_vendor (another Vendor instance): vendor to swap with
        Returns: True if the swap was completed, otherwise False
        '''

        if len(self.inventory) >= 1 and len(other_vendor.inventory) >= 1:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self,category):
        '''
        For a given item category, searches a vendor's inventory to find and 
            return the item in that category with the highest rated condition.
        Parameter: category (string): a string attribute for an item's type
        Returns: The highest rate item in that category, returns none if no 
            item in that category
        '''

        items_in_category = self.get_by_category(category)
        if len(items_in_category) > 0:
            items_in_category.sort(key=lambda item: item.condition, reverse=True)
            return items_in_category[0]
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Facilitates a swap between two vendors for the highest rated item
            of a desired category that the vendor specifies
        Parameters: 
            other (another Vendor instance): vendor to swap with
            my_priority (string): the desired type of item to swap for
            their_priority (string): the other vendor's desired type 
                of item to swap for
        Returns: True if the swap was completed, otherwise False
        '''
        
        best_their_priority = self.get_best_by_category(their_priority)
        best_my_priority = other.get_best_by_category(my_priority)
        if best_their_priority and best_my_priority:
            self.swap_items(other, best_their_priority, best_my_priority)
            return True
        return False