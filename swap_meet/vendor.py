class Vendor:
    def __init__(self, inventory = None):
        if inventory == None: 
            inventory = []
        self.inventory = inventory

    
    def add(self, item_added):
        self.inventory.append(item_added)
        return item_added
    
    def remove(self, item_removed):
        if item_removed in self.inventory:
            self.inventory.remove(item_removed)
            return item_removed
        else:
            return False

    def get_by_category(self, chosen_category):
        items_in_chosen_category = []
        for item in self.inventory:
            if item.category == chosen_category:
                items_in_chosen_category.append(item)
        return items_in_chosen_category
    
    def swap_items(self, friend, vender_item, friend_item):
        if vender_item in self.inventory and friend_item in friend.inventory:
            self.remove(vender_item)
            self.add(friend_item)
            friend.remove(friend_item)
            friend.add(vender_item)
            return True
        else: 
            return False
    
    def swap_first_item(self, friend):
        if len(self.inventory) != 0 and len(friend.inventory) != 0:
            first_item_vendor = self.inventory[0]
            first_item_friend = friend.inventory[0]
            return self.swap_items(friend, first_item_vendor, first_item_friend)

    def get_best_by_category(self, chosen_category):
        all_items_in_chosen_category = self.get_by_category(chosen_category)
        best_condition = 0
        if len(all_items_in_chosen_category) != 0:
            for item in all_items_in_chosen_category:
                best_condition = max(item.condition, best_condition)
            for item in all_items_in_chosen_category:
                if item.condition == best_condition:
                    return item
        return None
        
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        item_vendor_wanted = other.get_best_by_category(my_priority)
        item_other_wanted = self.get_best_by_category(their_priority)
        return self.swap_items(other, item_other_wanted, item_vendor_wanted)
     







