from types import NoneType
from operator import attrgetter


class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        #adds item to inventory
        self.inventory.append(item)
        return item

    def remove(self, item):
        # removes item from inventory if it's already there
        # if not, return false
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        # isolates all the items matching a specific category
        # and returns them in the form of a list
        self.category = category
        category_list = []
        for cat in self.inventory:
            if cat.category == self.category:
                category_list.append(cat)

        return category_list

    def get_best_by_category(self, category):
        # determine which item is in the best condition
        # for a given category
        best_item = None
        best_cat = 0

        # utilizing the get_by_category function to 
        # isolate the category
        best_cat = self.get_by_category(category)
        # if the function doesn't return a blank list
        if best_cat:
            # retreive the best condition

            # the attrgetter allows me to isolate and evaluate the condition
            # within the given instance
            best_item = max(best_cat, key=attrgetter("condition"))
        
        return best_item

    def swap_items(self, vendor2, my_item, their_item):
        # takes an item from first list and puts in it second
        # takes an item from second list and puts it in first
        self.vendor2 = vendor2
        self.my_item = my_item
        self.their_item = their_item

        if self.my_item not in self.inventory or self.their_item not in vendor2.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor2.inventory.append(my_item)
            vendor2.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, friend):
        # if neither list is empty then 
        # perform swap of first item in each list
        if not self.inventory or not friend.inventory:
            return False
        else:
            my_item = self.inventory[0]
            their_item = friend.inventory[0]

            self.swap_items(friend, my_item, their_item)
            return True

    def swap_best_by_category(self, other, my_priority, their_priority):
        # isolate each vendor's desired category
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        # if desired categories are found in the other person's list
        # then swap
        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other, my_item, their_item)
            return True