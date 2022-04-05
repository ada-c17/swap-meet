from inspect import trace
from .item import Item

class Vendor:
    # Additional attribute trait is added for the optional swap_by_newest function.
    # Trait can be Good or Evil, by default it is Good.
    # When there is an age tie for swap_by_newest, Good venodr swaps the item with the best condition,
    # While Evil vendor sawps the item with the worst condition
    def __init__(self, inventory=None, trait="Good"):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        self.trait = trait

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, new_item):
        if new_item in self.inventory:
            self.inventory.remove(new_item)
            return new_item
        return False
    
    # WAVE 2
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result
    
    # WAVE 3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(their_item)
            other_vendor.add(my_item)
            self.remove(my_item)
            other_vendor.remove(their_item)
            return True
        return False

    # WAVE 4
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_item, their_item)
            return True
        return False

    # WAVE 6
    def get_best_by_category(self, category):
        best_item = None
    
        for item in self.inventory:
            if item.category == category:
                if best_item == None:
                    best_item = Item(category=category)
                if item.condition > best_item.condition:
                    best_item = item 
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            self.swap_items(other, my_best, their_best)
            return True
        return False

    # OPTIONAL
    # returns the newest item (item.age is the smallest number) in the category
    # if no item in the category, return None
    # This is a helper function for swap_by_newest()
    def get_newest_by_category(self, category):
        category_list = self.get_by_category(category)

        if category_list:
            newest = category_list[0]

            for item in category_list:
                if item.age < newest.age:
                    newest = item
                elif item.age == newest.age:
                    if self.trait == "Good":
                        if item.condition > newest.condition:
                            newest = item
                    elif self.trait == "Evil":
                        if item.condition < newest.condition:
                            newest = item
            return newest
        return None
    
    # Swap the newest item in the category
    def swap_by_newest(self, other, my_priority, their_priority):
        my_newest = self.get_newest_by_category(their_priority)
        their_newest = other.get_newest_by_category(my_priority)
        if my_newest and their_newest:
            self.swap_items(other, my_newest, their_newest)
            return True
        return False







