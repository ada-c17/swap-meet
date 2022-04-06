from typing import ItemsView


class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item


    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.add(their_item)
            friend_vendor.add(my_item)
            self.remove(my_item)
            friend_vendor.remove(their_item)
            return True
        return False
    
    def swap_first_item(self,friend_vendor):
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False
        else:
            return self.swap_items(friend_vendor,self.inventory[0],friend_vendor.inventory[0])

    def get_best_by_category(self,category):
        best_condition = 0
        best_item = None
        items = self.get_by_category(category)
        for item in items:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self,other,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        return self.swap_items(other,my_best_item,their_best_item)
