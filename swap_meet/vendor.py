class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if category == item.category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            self.remove(my_item)
            other.add(my_item)
            
            other.remove(their_item)
            self.add(their_item)
        return True

    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        else:
            return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):

        condition_of_items_in_category = []

        for item in self.get_by_category(category):
                condition_of_items_in_category.append(item.condition)
        
        if not condition_of_items_in_category:
            return None

        best_condition = max(condition_of_items_in_category) #refactor with list comprehension?

        if not best_condition:
            return None
        
        for item in self.get_by_category(category):
            if item.condition == best_condition:
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
        
        condition_my_best_item = []
        for item in self.inventory:
            condition_my_best_item.append(item.condition)

        my_best_item = max(condition_my_best_item)

        condition_their_best_item = []
        for item in other.inventory:
            condition_their_best_item.append(item.condition)
        
        other_vendor_best_item = max(condition_their_best_item)

        my_trade_is_valid = False
        for item in self.get_by_category(their_priority):
            if item.condition == my_best_item:
                my_item = item
                my_trade_is_valid = True

        their_trade_is_valid = False
        for item in other.get_by_category(my_priority):
            if item.condition == other_vendor_best_item:
                their_item = item
                their_trade_is_valid = True

        if my_trade_is_valid and their_trade_is_valid:
            return self.swap_items(other, my_item, their_item)
