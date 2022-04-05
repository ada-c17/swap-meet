class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False 
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        list_items = []
        for item in self.inventory:
            if item.category == category:
                list_items.append(item)
        return list_items

    def swap_items(self, vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True
    
    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        my_first_item = self.inventory[0]
        friend_first_item = vendor.inventory[0]
        self.swap_items(vendor, my_first_item, friend_first_item)
        return True

    def get_best_by_category(self, category):
        highest_value = 0
        best_item = None
        try:
            for item in self.inventory:
                if item.category == category and item.condition >= highest_value:
                    highest_value = item.condition
                    best_item = item
        except IndexError:
            return None
            
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best is not None and their_best is not None:
            self.swap_items(other, my_best, their_best)
            return True
        return False

    def get_newest(self):
        try:
            newest_age = self.inventory[0].age
            newest_item = self.inventory[0]

            for i in range(1, len(self.inventory)):
                current_item = self.inventory[i]
                if current_item.age <= newest_age:
                    newest_age = current_item.age
                    newest_item = current_item
        except IndexError:
            return None
        
        return newest_item

    def swap_by_newest(self, other):
        my_newest = self.get_newest()
        their_newest = other.get_newest()

        if my_newest is None or their_newest is None:
            return False
        
        self.remove(my_newest)
        other.remove(their_newest)
        self.add(their_newest)
        other.add(my_newest)
        return True