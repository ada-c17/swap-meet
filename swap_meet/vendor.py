class Vendor:
    '''
    A class to represent a person.
    '''
    
    def __init__(self, inventory=None):
        '''Construct inventory attribute for vendor. Value of attribute is a list.
        '''
        self.inventory = inventory if inventory else []

    def add(self, new_item):
        '''
        add new item to person's inventory, return item
        '''
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        '''
        remove item from inventory, return item
        '''
        if item_to_remove not in self.inventory:
            return False
        self.inventory.remove(item_to_remove)
        return item_to_remove

    def get_by_category(self, category):
        '''
        make a list of given category and return it
        '''
        category_list = [item for item in self.inventory if item.category == category]
        return category_list

    def swap_items(self, friend, my_item, their_item):
        '''swap items from vendor inventory and friend inventory. Return True.
            If there are no items in vendor or friend inventory -> return False
        '''
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        return True

    def swap_first_item(self, friend):
        '''swap first items in vendor and friend inventories, return True.
           if one of inventories is empty, return False
        '''
        if not self.inventory or not friend.inventory:
            return False

        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        
        # [self.inventory[0], friend.inventory[0]] = [friend.inventory[0], self.inventory[0]]
        
        return True

    def get_best_by_category(self, category):
        '''get item with best condition in given category, return item.
           If no item matched given category -> return None
        '''
        category_list = [item for item in self.inventory if item.category == category]
        if not category_list:
            return None

        highest_condition = category_list[0].condition
        for item in category_list:
            if item.condition >= highest_condition:
                highest_condition = item.condition

        highest_items = [item for item in category_list if item.condition == highest_condition]
        return highest_items[0]

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''swap best itemof certain category with friend, return True. 
           If friend or vendor doesn't have items matched priorities
           in certain category -> return False.
        '''
        I_give = self.get_best_by_category(their_priority)
        friend_give = other.get_best_by_category(my_priority)
        if not I_give or not friend_give:
            return False
        self.swap_items(other, I_give, friend_give)
        return True
        
