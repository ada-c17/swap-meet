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

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            other_vendor.add(my_item)
            
            other_vendor.remove(their_item)
            self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.remove(self.inventory[0])
            other_vendor.add(my_first_item)
            
            thier_first_item = other_vendor.remove(other_vendor.inventory[0])
            self.add(thier_first_item)
        return True

    def get_best_by_category(self, category): #refactor to see if you can use get_category()

        condition_of_items_in_category = []

        for item in self.inventory:
            if category == item.category:
                condition_of_items_in_category.append(item.condition)
        
        if not condition_of_items_in_category:
            return None
        else:
            best_condition = max(condition_of_items_in_category)
        
        for item in self.inventory:
            if category == item.category and item.condition == best_condition:
                return item



        # if not get_category_items_list:
        #     return None
        # else:
        #     return max(get_category_items_list.item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
        
        this_vendor_condition_best_item = []
        other_vendor_condition_best_item = []

        for item in self.inventory:
            this_vendor_condition_best_item.append(item.condition)

        for item in other.inventory:
            other_vendor_condition_best_item.append(item.condition)
        
        this_vendor_best_condition = max(this_vendor_condition_best_item)
        other_vendor_best_condition = max(other_vendor_condition_best_item)

        my_trade_is_valid = False
        for item in self.inventory:
            if their_priority == item.category and item.condition == this_vendor_best_condition:
                my_item = item
                my_trade_is_valid = True

        their_trade_is_valid = False
        for item in other.inventory:
            if my_priority == item.category and item.condition == other_vendor_best_condition:
                their_item = item
                their_trade_is_valid = True

        if my_trade_is_valid and their_trade_is_valid:
            self.remove(my_item)
            other.add(my_item)
            
            other.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False