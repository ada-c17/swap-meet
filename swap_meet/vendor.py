class Vendor:
    '''
    A class to represent a vendor at the swap meet.

    ...

    ---Attributes---
    inventory : list, optional
        None by default, else a list of the vendor's items

    ---Methods---
    add(one_item):
        adds one_item to the instance's inventory list
    remove(one_item):
        if items in inventory, removes and returns one_item, else returns False
    get_by_category(category_to_check):
        takes a cateogry and returns a list of the items currently in the instance's inventory with that category attribute
    swap_items(swap_friend, my_item, their_item):
        takes another vendor's item and an item from the current vendor and swaps them
    swap_first_item(swap_friend):
        takes the first item of the current instance's inventory and the first item of swap_friend's inventory and swaps them
    get_best_by_category(category):
        searches an instance's inventory attribute for an item of a specific category with the highest condition and returns it
    swap_best_by_category(other, my_priority, their_priority):
        swaps the best items in the specified priority categories between the current instance's inventory and the other instance's inventory
    '''
    def __init__(self, inventory=None):
        '''
        Constructs all the necessary attributes for the vendor object

        ---Paramters---
        inventory : list, optional
            a list of item objects (default is None)
        '''
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, one_item):
        '''Adds one_item to the instance's inventory list'''
        self.inventory.append(one_item)
        return one_item

    def remove(self, one_item):
        '''
        If items in inventory, removes and returns one_item, else returns False
        '''
        try:
            self.inventory.remove(one_item)
            return one_item
        except ValueError:
            return False
        
    def get_by_category(self, category_to_check):
        '''
        Takes a cateogry and returns a list of the items currently in the instance's inventory with that category attribute
        '''
        list_by_cat = [item for item in self.inventory if item.category == category_to_check]
        return list_by_cat

    def swap_items(self, swap_friend, my_item, their_item):
        '''
        Takes another vendor's item and an item from the current vendor and swaps them

        ---Parameters---
        swap_friend : Vendor instance
            the vendor to swap items with
        my_item : Item instance
            the item from the current instance's inventory to swap
        their_item : Item instance
            the item from swap_friend's inventory to swap

        ---Returns---
        Returns true if both items are in their respective inventories and the items were switched, otherwise returns False
        '''
        if my_item not in self.inventory:
            return False
        if their_item not in swap_friend.inventory:
            return False
        self.remove(my_item)
        swap_friend.add(my_item)
        swap_friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, swap_friend):
        '''
        Takes the first item of the current instance's inventory and the first item of swap_friend's inventory and swaps them
        '''
        if not self.inventory or not swap_friend.inventory:
            return False
        my_item = self.inventory.pop(0)
        their_item = swap_friend.inventory.pop(0)
        self.add(their_item)
        swap_friend.add(my_item)
        return True
        
    def get_best_by_category(self, category):
        '''
        Searches an instance's inventory attribute for an item of a specific category with the highest condition and returns it
        '''
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        best_condition = max(category_list, key=lambda x: x.condition).condition
        for item in category_list:
            if item.condition == best_condition:
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Swaps the best items in the specified priority categories between the current instance's inventory and the other instance's inventory

        ---Parameters---
        other : Vendor instance
            the vendor to swap items with
        my_priority : str
            the category of item to be searched for in the other inventory
        their_priority : str
            the category of item to be searched for in the current instance's inventory  

        ---Returns---
        Returns False if there were no items of category my_priority in other's inventory or if there were no items of category their_priority in the current instance's inventory. Returns true if these exist and were swapped.
        '''
        to_trade = self.get_best_by_category(their_priority)
        to_receive = other.get_best_by_category(my_priority)
        if not to_trade or not to_receive:
            return False
        return self.swap_items(other, to_trade, to_receive)
