
class Vendor:
    '''
    Instances of Vendor Class represent a vendor at a swap
    meet. Their inventory attribute stores a list of
    instances of Item classes, representing the items
    they are bringing to the swapmeet.
    '''
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, new_item):
        '''
        Add an item to a vendor's inventory list.

        Parameters - 
            Item to be added.
        Returns -
            Item that was added.
        '''
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):

        '''
        Remove an item from a vendor's inventory list.
        
        Parameters - 
            Item to be removed.
        Returns -
            Item that was removed.
        '''

        try:
            self.inventory.remove(item)
        except(ValueError):
            return False
        return item

    def get_by_category(self, category_to_search):

        '''
        Parameters - 
            Desired category to be searched

        Returns - 
            List of items in vendor's inventory matching
            the desired categpry.
        '''

        return_list = []
        for item in self.inventory:
            if item.category == category_to_search:
                return_list.append(item)
        return return_list

    def swap_items(self, other_vendor, my_item, their_item):
        '''
        Swaps two Vendors' items and updates their inventories to reflect the swap.

        Parameters - 
            Other Vendor, Item to be swapped from self, Item to be swapped from the other vendor.

        Returns -
            Boolean based on if the items are present in the correct inventories.

        '''

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))

        return True

    def swap_first_item(self, other_vendor):
        '''
        Swaps the first item in two vendors' inventories and updates their inventories to reflect the swap.

        Parameters - 
            Other Vendor

        Returns -
            Boolean based on if both of the vendors have at least 1 item in their inventories.

        '''

        try:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        except IndexError:
            return False

        return True

    def get_best_by_category(self, desired_category):
        '''
        Gets the highest rated item of specific category.

        Parameters - 
            Desired category
        
        Returns - 
            Highest rated item in desired category if it exists
            Returns None otherwise
        '''
        try:
            return max(self.get_by_category(desired_category) , key = lambda x: x.condition)
        except ValueError:
            return None


    def swap_best_by_category(self, other, my_priority, their_priority):
        
        '''
        Swaps highest rated items of specific category between two vendors.

        Parameters - 
            Other Vendor, desired category to be swapped from self, desired category to be swapped from the other vendor.

        Returns -
            Boolean based on if the items are present in the correct inventories.

        '''
        
        my_highest_rated = self.get_best_by_category(their_priority)
        their_highest_rated = other.get_best_by_category(my_priority)
        
        if my_highest_rated and their_highest_rated:
            self.swap_items(other, my_highest_rated, their_highest_rated)
            return True
        else:
            return False