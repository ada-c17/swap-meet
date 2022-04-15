
from swap_meet.item import Item

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
        except Exception:
            return False

    def get_by_category(self, category):
        items_by_category = []

        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        
        return items_by_category
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False


        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True

    
    def get_best_by_category(self, category):
        
        best_condition_so_far = 0
        
        list_of_items_by_category = self.get_by_category(category)
        if list_of_items_by_category == None:
            return None
        for item in list_of_items_by_category:
            if item.condition > best_condition_so_far:
                best_condition_so_far = item.condition
        for item in list_of_items_by_category:
            if item.condition == best_condition_so_far:
                return item

    def swap_best_by_category(self, other, my_priority, their_priority):

        self_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, self_best_item, their_best_item)
