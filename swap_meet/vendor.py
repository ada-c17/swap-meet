from unicodedata import category
from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory 
            

    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False


    def get_by_category(self, category):
        if not category:
            return False
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list 


    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in friend.inventory:
            return False

        self.inventory.remove(my_item)
        friend.inventory.append(my_item) 
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)

        if their_item not in self.inventory:
            return False
        else:
            return True


    def swap_first_item(self, friend):
        if self.inventory == []:
            return False
        else: 
            my_item = self.inventory[0]
        if friend.inventory == []:
            return False
        else:
            their_item = friend.inventory[0]
        # use swap_items method
        self.swap_items(friend, my_item, their_item)
        return True


    def get_best_by_category(self, category):
        desired_category = []

        for item in self.inventory:
            if category in item.category:
                desired_category.append(item)
        # lambda will sort objects by instance's "condtion" attribute
                sort_list = sorted(desired_category, key=lambda item: item.condition)
        if desired_category == []:
            return None
        return sort_list[-1]    


    def swap_best_by_category(self, other, my_priority, their_priority):
        # created variables for self and other to use the get_best_by_category method
        their_desired_item = self.get_best_by_category(their_priority)
        my_desired_item = other.get_best_by_category(my_priority)
        
        if their_desired_item is None or my_desired_item is None:
            return False
        self.swap_items(other, their_desired_item, my_desired_item)
        return True
