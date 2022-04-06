class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items
    
    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        another_vendor.add(my_item)
        another_vendor.remove(their_item)
        return True
    
    def swap_first_item(self, another_vendor):
        if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
            return False
        self.swap_items(another_vendor, self.inventory[0], another_vendor.inventory[0])
        return True

    def get_best_by_category(self, category):
        high_condition = 0
        matching_item = None

        for item in self.inventory:
            if item.category == category and item.condition > high_condition:
                high_condition = item.condition
                matching_item = item
            
        return matching_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        my_swap_item = other.get_best_by_category(my_priority)
        their_swap_item = self.get_best_by_category(their_priority)
        swap_items_result = self.swap_items(other, their_swap_item, my_swap_item)
        
        return swap_items_result



