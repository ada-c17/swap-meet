class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, specific_category):
        category_matches = []
        for item in self.inventory:
            if item.category == specific_category:
                category_matches.append(item)
        return category_matches

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        '''
        1) Adds the first item from Jolie's (friend's) inventory.
        2) Removes first item from Fatimah's (self's) inventory.
        3) Adds the instances first item
        4) Remove the first item from Jolie's inventory
        '''
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])

            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        return False
    
    def get_best_by_category(self, specific_category):
        best_by_category = None
        highest_condition = 0
        
        for item in self.inventory:
            if item.category == specific_category and item.condition > highest_condition:
                    best_by_category = item
                    highest_condition = item.condition

        return best_by_category
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        1) The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches 
            It returns `True`
        2) If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
        3) If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False  `
        '''
        # if my_priority in other.inventory
        test = 0
        my_best_item = None
        for item in other.inventory:
            if item.category == my_priority and item.condition > test:
                test = item.condition
                my_best_item = item
        
        test2 = 0
        their_best_item = None
        for item in self.inventory:
            if item.category == their_priority and item.condition > test:
                test_2 = item.condition
                their_best_item = item
               
        # if best_item:
        #     return True
        # return False