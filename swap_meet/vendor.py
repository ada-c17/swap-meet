class Vendor:

    def __init__(self, inventory=None):

        if inventory is None:
            self._inventory = []
        else:
            self._inventory = inventory


    @property
    def inventory(self):       
        # make inventory a read-only attribute
        # changes to inventory should only be done via add() & remove()
        
        return self._inventory


    def add(self, item):

        self._inventory.append(item)
        return item


    def remove(self, item):

        item_index = self.get_item_index(item)

        if item_index == -1:
            return False

        del self._inventory[item_index]

        return item


    def get_item_index(self, item):

        try:
            return self._inventory.index(item)
            
        except ValueError:
            return -1


    def get_by_category(self, category):

        return [item for item in self._inventory if item.category == category]

    
    def swap_items(self, other, my_item, their_item):

        my_item_index = self.get_item_index(my_item)
        their_item_index = other.get_item_index(their_item)

        if my_item_index == -1 or their_item_index == -1:
            return False
        
        self._inventory[my_item_index], other._inventory[their_item_index] = their_item, my_item
        
        return True

    
    def swap_first_item(self, other):

        if not self._inventory or not other._inventory:
            return False
        
        return self.swap_items(other, self._inventory[0], other._inventory[0])


    def get_best_by_category(self, category):

        best_item = None

        items_in_category = self.get_by_category(category)

        if items_in_category:
            for item in items_in_category:
                if best_item is None or item.condition > best_item.condition:
                    best_item = item
        
        return best_item

    
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False
        
        else:
            return self.swap_items(other, my_item, their_item)
    

    def get_newest_item(self):
        
        newest_item = None
        smallest_age = None

        for item in self._inventory:
            if item.age and (not smallest_age or item.age < smallest_age):
                newest_item = item
                smallest_age = item.age
        
        return newest_item


    def swap_by_newest(self, other):

        my_newest = self.get_newest_item()
        their_newest = other.get_newest_item()

        if not my_newest or not their_newest:
            return False

        return self.swap_items(other, my_newest, their_newest)