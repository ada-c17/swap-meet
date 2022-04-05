class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory


    def add(self, item):

        self.inventory.append(item)
        return item


    def remove(self, item):
        item_index = self.get_item_index(item)

        if item_index == -1:
            return False

        del self.inventory[item_index]

        return item


    def get_item_index(self, item):
        try:
            return self.inventory.index(item)
        except ValueError:
            return -1


    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]


    def swap_items(self, other, my_item, their_item):

        my_item_index = self.get_item_index(my_item)
        their_item_index = other.get_item_index(their_item)

        if my_item_index == -1 or their_item_index == -1:
            return False
        
        self.inventory[my_item_index], other.inventory[their_item_index] = their_item, my_item
        
        return True

    
    def swap_first_item(self, other):

        if not self.inventory or not other.inventory:
            return False
        
        return self.swap_items(other, self.inventory[0], other.inventory[0])


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