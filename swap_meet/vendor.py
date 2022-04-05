class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self, one_item):
        self.inventory.append(one_item)
        return one_item

    def remove(self, one_item):
        try:
            self.inventory.remove(one_item)
            return one_item
        except ValueError:
            return False
        
    def get_by_category(self, category_to_check):
        list_by_cat = [item for item in self.inventory if item.category == category_to_check]
        return list_by_cat

    def swap_items(self, swap_friend, my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in swap_friend.inventory:
            return False
        self.remove(my_item)
        swap_friend.add(my_item)
        swap_friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, swap_friend):
        if not self.inventory or not swap_friend.inventory:
            return False
        my_item = self.inventory.pop(0)
        their_item = swap_friend.inventory.pop(0)
        self.add(their_item)
        swap_friend.add(my_item)
        return True
        
    def get_best_by_category(self, category):
        # if not category:
        #     return None
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        best_condition = max(category_list, key=lambda x: x.condition).condition
        for item in category_list:
            if item.condition == best_condition:
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        to_trade = self.get_best_by_category(their_priority)
        to_receive = other.get_best_by_category(my_priority)
        if not to_trade or not to_receive:
            return False
        return self.swap_items(other, to_trade, to_receive)
