# from swap_meet.item import Item
from operator import attrgetter
import copy

class Vendor:
    
    def __init__(self, inventory = []):
        self.inventory = copy.copy(inventory)
    
    def add(self, it):
        self.inventory.append(it)
        return it
    
    def remove(self, it):
        if it in set(self.inventory):
            self.inventory.remove(it)
            return it
        else:
            return False
    
    def get_by_category(self, category):
        cat_list = []
        for i in self.inventory:
            if i.category == category:
                cat_list.append(i)
        return cat_list
    
    def swap_items(self, other, my_item, their_item):
        if my_item in self.inventory:
            self.remove(my_item)
            other.add(my_item)
        else:
            return False
        if their_item in other.inventory:
            other.remove(their_item)
            self.add(their_item)
        else:
            self.add(my_item)
            other.remove(my_item)
            return False
        return True
    
    def swap_first_item(self, other):
        if len(self.inventory) >= 1 and len(other.inventory) >= 1:
            other.add(self.inventory[0])
            self.remove(self.inventory[0])
            self.add(other.inventory[0])
            other.remove(other.inventory[0])
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) < 1:
            return None
        best_condition = 0
        for i in items_in_category:
            if i.condition > best_condition:
                best_condition = i.condition
                best_item = i
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_choice = other.get_best_by_category(my_priority)
        their_choice = self.get_best_by_category(their_priority)
        if my_choice and their_choice:
            self.remove(their_choice)
            other.remove(my_choice)
            other.add(their_choice)
            self.add(my_choice)
            return True
        else:
            return False