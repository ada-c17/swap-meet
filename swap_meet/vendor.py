class Vendor:
    def __init__(self, inventory = None):
        '''
        Its parameter inventory is an empty list
        '''
        if not inventory:
            inventory = []
        self.inventory  = inventory

    def add(self, add_item):
        '''
        It adds item to the inventory.
        Argument - add_item(string): representing an item
        Return: the item that was added 
        '''
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        '''
        It removes the matching item from the inventory.
        Argument - remove_item(string): representing an item
        Return: the item that was removed, if there is no matching item it returns False
        '''
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False

    def get_by_category(self, category):
        '''
        It gets a list of the inventory and its category
        Argument - category(string): representing a category
        Return: a list of Items in the inventory with that category
        '''
        results = []
        for item in self.inventory:
            if category == item.category:
                results.append(item)
        return results

    def swap_items(self, another_vendor, my_item, their_item):
        '''
        It swaps my item and my friend's item
        Argument - 
            another_vendor: the friend whom I(vendor but I will say I) am swapping my item with
            my_item: the item I give to the friend
            their_item: the item my friend gives to me
        Return: if my inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, it returns False, otherwise returns True
        '''
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        '''
        Hi Audrey, I have two options here. 1. line 58 ~ 65, 2. line 68 ~ 71 
        Which way would be a better way? :) 

        another way of writing line  
        my_inventory = self.inventory
        friend_inventory = another_vendor.inventory

        my_inventory.remove(my_item)
        friend_inventory.append(my_item)
        friend_inventory.remove(their_item)
        my_inventory.append(their_item)
        '''

        self.inventory.remove(my_item)
        another_vendor.inventory.append(my_item)
        another_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True
    
    def swap_first_item(self, another_vendor):
        '''
        A method of the class Vendor. It swaps both my and my friend's first item
        Argument - another_vendor: the friend whom I am swapping my item with
        Return: if either the friend or I have an empty inventory, it returns False, otherwise returns True
        '''
        if not another_vendor.inventory or not self.inventory:
            return False
        
        self.swap_items(another_vendor, self.inventory[0], another_vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        '''
        A method of the class Vendor. This method looks through the instance's inventory for the item with the highest condition and matching category
        Argument - category: representing a category
        Return: the item with the best condition in a category
        '''
        category_inventories = self.get_by_category(category)
        if not category_inventories:
            return None

        best_item = category_inventories[0]
        for item in category_inventories:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        A method of the class Vendor. This method swaps the best item of certain categories with friend
        Argument - 
            other: the friend whom I am swapping the item with
            my_priority: a category that I want to get from my friend's inventory
            their_priority: a category that my friend wants to get from my inventory
        Return: True, if the best item in my inventory that matches my friend's priority and the best item in my friend's that matches my priority. Otherwise returns False
        '''
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False

        self.swap_items(other, my_best, their_best)
        return True