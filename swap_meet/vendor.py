from .item import Item


class Vendor:
    def __init__(self, inventory= None): 
        self.inventory = inventory if inventory is not None else []
    
# Methods 

    def add(self, item):
        ''' adds item to inventory '''
        self.inventory.append(item)
        return item 


    def remove(self, other_item):
        ''' removes duplicate item if true '''
        if other_item in self.inventory:
            self.inventory.remove(other_item)
            return other_item
        else:
            return False

    def get_by_category(self, category):
        ''' returns a list of items in the inventory
            if item category matches item category in inventory
        '''
        list_of_items= []
        for item in self.inventory:
            if item.category == category:
                list_of_items.append(item)
        return list_of_items


    def swap_items(self, vendor_friend, my_item, their_item):
        '''
        return False if inventory doesn't contain my_item or 
        vendor friend doesn't contain their_item

        return True 
        '''
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        else:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True

    def swap_first_item(self, swapping_friend):
        '''
        if self.inventory or swapping_friend.inventory
        are empty, return False

        remove 1st item from self.inventory add swapping_friend 1st item
        remove ""       ""   swapping_friend.inventory add self.inventory ""
        return True
        '''

            
        if not self.inventory or not swapping_friend.inventory:
            return False
        else:
            self.add(swapping_friend.inventory[0])
            swapping_friend.add(self.inventory[0])
            self.remove(self.inventory[0])
            swapping_friend.remove(swapping_friend.inventory[0])
            return True
    
    def get_best_by_category(self, a_category):
        '''iterate through this instance's inventory for item.category 
            highest rating from 0-5
            return item 
            else return None 
        '''
            
        items_in_category = self.get_by_category(a_category)
        highest_rating = 0
        highest_item = None
        for item in items_in_category:
            if item.condition > highest_rating:
                highest_rating = item.condition
                highest_item = item 

        return highest_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''self and instance of vendor other want to swap items
        of their category of choice with the best rating
        return false if category not in their inventory
        else: swap and return true '''
        other_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if not my_item or not other_item:
            return False
        return self.swap_items(other, my_item, other_item)
    

        






