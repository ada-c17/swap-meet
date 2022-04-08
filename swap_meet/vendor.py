class Vendor:
    
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in set(self.inventory):
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        cat_list = []
        for item in self.inventory:
            if item.category == category:
                cat_list.append(item)
        return cat_list
    
    def swap_items(self, other, my_item, their_item):
        try:
            my_index = self.inventory.index(my_item)
            their_index = other.inventory.index(their_item)
            self.inventory[my_index], other.inventory[their_index] = other.inventory[their_index], self.inventory[my_index]
            return True
        except:
            return False
    
    def swap_first_item(self, other):
        if len(self.inventory) >= 1 and len(other.inventory) >= 1:
            self.inventory[0], other.inventory[0] = other.inventory[0], self.inventory[0]
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) < 1:
            return None
        elif len(items_in_category) == 1:
            return items_in_category[0]
        best_item = max(items_in_category, key=lambda item: item.condition)
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_choice = other.get_best_by_category(my_priority)
        their_choice = self.get_best_by_category(their_priority)
        if my_choice and their_choice:
            self.swap_items(other, their_choice, my_choice)
            return True
        else:
            return False
    
    def swap_by_newest(self, other):
        if self.inventory and other.inventory:
            my_newest_item = min(self.inventory, key=lambda item: item.age)
            their_newest_item = min(other.inventory, key=lambda item: item.age)
            self.swap_items(other, my_newest_item, their_newest_item)
        else:
            return None