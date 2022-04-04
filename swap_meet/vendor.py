
class Vendor:
    def __init__(self, inventory= []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            del self.inventory[self.inventory.index(item)]
            return item
        return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):

        if my_item not in self.inventory or their_item not in other.inventory:
            return False
            
        self.add(their_item)
        self.remove(my_item)
        other.add(my_item)
        other.remove(their_item)
        return True

    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        else:
            self.inventory[0], other.inventory[0] = other.inventory[0], self.inventory[0]
            return True
        