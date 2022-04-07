

class Vendor:
    '''
    Vendor class has an attribute named inventory which starts as an empty list by default and complete 
    methods such as adding, removing, swapping, and figuring out best categories in your inventory and 
    your friend's inventory.
    '''
    
    def __init__(self, inventory = None):
        '''
        Attribute named inventory which starts as an empty list by default, but can be pass in a list.
        '''
        if not inventory:
            inventory = []
        self.inventory = inventory

    
    def add(self, add_item):
        '''
        Instance method that takes in an item and add it to the inventory list and return the item that was added.
        '''
        self.inventory.append(add_item)
        return add_item

    def remove(self, remove_item):
        '''
        Instance method that removes an item from the inventory list and return the item that was removed.
        '''
        if remove_item in self.inventory:
            self.inventory.remove(remove_item)
            return remove_item
        else:
            return False

    def get_by_category(self, category):
        '''
        Instance method that takes in a category string and returns a list of items in the inventory with that category.
        '''
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        return category_list

    def swap_items(self, friend_vendor, my_item, their_item):
        '''
        Instance method that takes in three arguments which swap items from your inventory to your friend's inventory and vice versa.
        '''
        if my_item not in self.inventory or their_item not in friend_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        friend_vendor.inventory.append(my_item)
        friend_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, friend_vendor):
        '''
        Instance method that takes in three arguments which swap first item from your inventory to your friend's inventory and vice versa.
        '''
        if self.inventory == [] or friend_vendor.inventory == []:
            return False
        friend_vendor.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        self.inventory.append(friend_vendor.inventory[0])
        friend_vendor.inventory.remove(friend_vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        '''
        Instance method that will return the item with the best condition in a certain category. 
        '''
        new_category = self.get_by_category(category)
        if not new_category:
            return None
        best = new_category[0]
        for item in new_category:
            if item.condition > best.condition:
                best = item
        return best
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Instance method that will swap the item with the best condition in a certain category from your inventory to your friends and vice versa.
        '''
        my_best_category = self.get_best_by_category(their_priority)
        their_best_category = other.get_best_by_category(my_priority)
        if not their_best_category or not my_best_category:
            return False
        self.swap_items(other, my_best_category, their_best_category)
        return True


