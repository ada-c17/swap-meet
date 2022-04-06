'''
Vendor class represents individuals trading at swap meet.
Includes the attribute 'inventory', which is a list of Item instances.
Includes numerous methods to work with and modify vendors' inventories.
'''


class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''
        Adds one item to vendor's inventory and returns item. 
        Helper function to swap_items method.
        '''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''
        Removes one item from vendor's inventory and returns item. 
        Returns False if item not found in inventory. 
        Helper function to swap_items method.
        '''
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        '''
        Takes a category as parameter and returns instance's inventory list filtered to only items belonging to that category.
        Returns empty list if none found. 
        Helper function to get_best_by_category method.
        '''
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, item_given, item_received):
        '''
        Receives parameters of other vendor instance, item to give that instance and item to receive from that instance. 
        Swaps two items between the vendor instance's inventory and other vendor instance's inventory. 
        Returns True if successful and False if either item is not found in inventory. 
        Helper function to several other methods.
        '''
        if item_given not in self.inventory or item_received not in other.inventory:
            return False

        self.remove(item_given)
        self.add(item_received)
        other.remove(item_received)
        other.add(item_given)
        return True

    def swap_first_item(self, other):
        '''
        Receives other vendor instance as parameter. 
        Trades the first item listed in vendor instance's inventory with the first item listed in other vendor instance's inventory. 
        Returns True if successful and False if either inventory is falsey.
        '''
        if not self.inventory or not other.inventory:
            return False
        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        '''
        Returns the highest-rated item in instance's inventory belonging to the category passed in as a parameter. 
        Helper method to swap_best_by_category method.
        '''
        category_inventory = self.get_by_category(category)
        if len(category_inventory) < 1:
            return None
        best_item = category_inventory[0]
        for item in category_inventory:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Receives parameters of another vendor instance, preferred category for self instance and preferred category for other instance. 
        Swaps the highest-rated item in each instance's inventory belonging to the category preferred by the other instance.
        Returns True if successful and False if either item can't be found.
        '''
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        return self.swap_items(other, my_best, their_best)

    def get_newest(self):
        '''
        Returns the item in inventory attribute with the lowest age attribute. 
        Returns False if any item missing age attribute.
        Helper function to swap_by_newest function.
        '''
        newest = self.inventory[0]
        for item in self.inventory:
            if not item.age:
                return False
            if item.age < newest.age:
                newest = item
        return newest

    def swap_by_newest(self, other):
        '''
        Receives another vendor instance as parameter and trades the newest item from each vendor instance's inventory.
        Returns False if either inventory does not have an identifiable newest item.
        '''
        my_newest = self.get_newest()
        their_newest = other.get_newest()
        if not my_newest or not their_newest:
            return False
        return self.swap_items(other, my_newest, their_newest)
