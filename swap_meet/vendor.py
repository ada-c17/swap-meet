from unicodedata import category
from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory 
            

    def add(self, item):
        # if item exists, append item to inventory
        self.inventory.append(item)
        # return statment with item added
        return item


    def remove(self, item):
        # takes in item and removes matching item 
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
        
        self.swap_items(friend, my_item, their_item)
        return True
        

    def get_best_by_category(self, category):
        # create empty list to hold category vender wants
        desired_category = []
        # iterate through items in self inventory
        for item in self.inventory:
        #     if category != items.category:
        #         return None
        # if the category the vender wants is one of the categories
            if category in item.category:
        #  append the item to the list of desired categories
                desired_category.append(item)
        # sort the desired category to get the best condition
        # use of lambda to sort objects by instance's "condtion" attribute
                sort_list = sorted(desired_category, key=lambda item: item.condition)
        # if the list of desired categories is empty, return none
        if desired_category == []:
            return None
        # if not, return sorted [-1]
        return sort_list[-1]


        
    
        # ? sort so that condition ordered by keys
    

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_desired_item = self.get_best_by_category(their_priority)
        my_desired_item = other.get_best_by_category(my_priority)
        
        # start with checking if the priorities exist
        # in both self and other
        # check to see if swap occured 
        if their_desired_item is None or my_desired_item is None:
            return False
        self.swap_items(other, their_desired_item, my_desired_item)
        return True
        