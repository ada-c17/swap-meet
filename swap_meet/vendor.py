from .item import Item
class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
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
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
    
    
    def swap_items(self, vendor_friend, my_item, their_item):
        
        if my_item in self.inventory and their_item in vendor_friend.inventory:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
    
    
    def swap_first_item(self, vendor_friend):
        if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
            return False
        self.add(vendor_friend.inventory[0])
        vendor_friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        vendor_friend.remove(vendor_friend.inventory[0])
        return True
    
    
    def get_best_by_category(self, category ):
        category_list = self.get_by_category(category)
        if category_list == []:
            return None
        best_condition = category_list[0]
        for item in category_list:
            if item.condition > best_condition.condition:
                best_condition = item
        return best_condition
    
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_category = self.get_best_by_category(their_priority)
        their_best_category = other.get_best_by_category(my_priority)
        if my_best_category and their_best_category:
            self.swap_items(other, my_best_category, their_best_category)
            return True
        return False
            
            
    def newest_item(self):
        if self.inventory == []:
                return None
        new_item = self.inventory[0]
        for item in self.inventory:
            if item.age < new_item.age:
                new_item = item       
        return new_item
    
    def swap_by_newest(self, vendor_friend):
        my_new_item = self.newest_item()
        friend_new_item = vendor_friend.newest_item()
        return self.swap_items(vendor_friend,my_new_item , friend_new_item)
        
            