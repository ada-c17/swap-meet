class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item


    def get_by_category(self, category):
        item_list = [item for item in self.inventory if item.category == category]
        return item_list

    def swap_items(self, friend_vendor, my_item, friend_item):
        if my_item not in self.inventory or friend_item \
            not in friend_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(friend_item)
        friend_vendor.inventory.remove(friend_item)
        friend_vendor.inventory.append(my_item)
        return True
    
    def swap_first_item(self, friend_vendor):
        if not self.inventory or not friend_vendor.inventory:
            return False 
        self.inventory.append(friend_vendor.inventory[0])
        friend_vendor.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        friend_vendor.inventory.pop(0)
        return True
    
    def get_best_by_category(self, category):
        max_condition = 0
        max_item = None
        for item in self.inventory:
            if item.category == category and item.condition >= max_condition:
                max_item = item 
                max_condition = item.condition
        return max_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True



