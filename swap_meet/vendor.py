from operator import attrgetter

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 
    
    def get_by_category(self, category):
        same_catagory_items = []
        for item in self.inventory:
            if item.category == category:
                same_catagory_items.append(item)
        return same_catagory_items


    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory:
            return False
        elif their_item not in friend_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            friend_vendor.remove(their_item)
            friend_vendor.add(my_item)
        return self.inventory 

    def swap_first_item(self, friend_vendor):
        if self.inventory == [] or friend_vendor.inventory == []:
            return False
        else:
            self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])
            return True

    def get_best_by_category(self, category):
        similiar_items = []
        for item in self.inventory:
            if item.category == category:
                similiar_items.append(item)
        if len(similiar_items) == 0:
            return None
        best_condition_item = max(similiar_items, key=attrgetter('condition'))
        return best_condition_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_offer = other.get_best_by_category(my_priority)
        my_offer = self.get_best_by_category(their_priority)
        if their_offer == None or my_offer == None:
            return False
        else:
            self.swap_items(other, my_offer, their_offer)
            return True