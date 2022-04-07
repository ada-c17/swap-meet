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
        if my_item in self.inventory:
            self.remove(my_item)
            other.add(my_item)
        else:
            return False
        if their_item in other.inventory:
            other.remove(their_item)
            self.add(their_item)
        else:
            self.add(my_item)
            other.remove(my_item)
            return False
        return True
    
    def swap_first_item(self, other):
        if len(self.inventory) >= 1 and len(other.inventory) >= 1:
            self.swap_items(other, self.inventory[0], other.inventory[0])
            return True
        else:
            return False
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) < 1:
            return None
        best_condition = 0
        for item in items_in_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
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
            my_newest_item = min(self.inventory, key=lambda x: x.age)
            their_newest_item = min(other.inventory, key=lambda x: x.age)
            self.swap_items(other, my_newest_item, their_newest_item)
        else:
            return None