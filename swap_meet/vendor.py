from typing import ItemsView


class Vendor:
    #Wave 1
    ''' We are creating an inventory, which is an empty list, for storing,removing and adding items'''
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
    
    #Wave 2
    '''Returns a list of items in the inventory with that category'''
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    #Wave 3
    '''Swap item between self inventory and friend inventory, returns a boolean'''
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in friend_vendor.inventory:
            self.add(their_item)
            friend_vendor.add(my_item)
            self.remove(my_item)
            friend_vendor.remove(their_item)
            return True
        return False
    
    #Wave 4
    '''Swap the first item, returns a boolean.'''
    def swap_first_item(self,friend_vendor):
        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False
        else:
            return self.swap_items(friend_vendor,self.inventory[0],friend_vendor.inventory[0])
    
    #Wave 6
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

    #Enhancements 
    '''Creating an instance method find_newest_item to get the item that has smallest age'''
    def find_newest_item(self,inventory):
        newest_age = inventory[0].age
        newest_item = None
        for item in inventory:
            if item.age < newest_age:
                newest_age = item.age
                newest_item = item
        return newest_item      

    '''swap the newest item in self inventory and friend inventory'''
    def swap_by_newest(self,friend_vendor):
        my_newest_item = None
        their_newest_item = None

        if len(self.inventory) == 0 or len(friend_vendor.inventory) == 0:
            return False
        
        else:
            my_newest_item = self.find_newest_item(self.inventory)
            their_newest_item = friend_vendor.find_newest_item(friend_vendor.inventory)
            return self.swap_items(friend_vendor,my_newest_item,their_newest_item)
    


