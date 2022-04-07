
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try: 
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        #  ValueError will be raised if item not in self.inventory

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False    

        self.add(their_item)
        other.add(my_item)
        self.remove(my_item)
        other.remove(their_item)
        return True
    
    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False

        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        
        try:
            return max(items_in_category, key=lambda item: item.condition)
        except ValueError:
            #  ValueError will be raised if items_in_category is empty
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_item, their_item)

    def get_newest(self):
        try:
            return min(self.inventory, key=lambda item: item.age)
        except ValueError:
            #  ValueError will be raised if self.inventory is empty
            return None

    def swap_by_newest(self, other):
        my_item = self.get_newest()
        their_item = other.get_newest()
        
        return self.swap_items(other, my_item, their_item)