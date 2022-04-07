from re import A
from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory =[]
        else:
            self.inventory = inventory
        
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items=[]
        for item in self.inventory:
            if str(item.category) == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in another_vendor.inventory:    
            return False
        
        another_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        another_vendor.inventory.remove(their_item)
        return True
            
    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        self.inventory.append(friend.inventory[0])
        friend.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        friend.inventory.remove(friend.inventory[0])
        return True

    def get_best_by_category(self, category):
        matched_category=[]
        for item in self.inventory:
            if item.category == category:
                matched_category.append(item)

        if len(matched_category) == 0:
            return None
        highest_condition = matched_category[0]
        for item in matched_category:
            if item.condition > highest_condition.condition:
                highest_condition = item
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        return False
            
    def swap_by_newest(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return None
        my_newest_item = self.inventory[0]
        for item in self.inventory:
            if item.age < my_newest_item.age:
                my_newest_item = item

        friend_newest_item = friend.inventory[0]
        for item in friend.inventory:
            if item.age < friend_newest_item.age:
                friend_newest_item = item

        self.swap_items(friend, my_newest_item, friend_newest_item)
        return True


    
    
            

        


        