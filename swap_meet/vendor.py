class Vendor:
    
    def __init__(self, inventory = []):
        self.inventory = inventory
    
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
        for i in self.inventory:
            if i.category == category:
                cat_list.append(i)
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
            other.add(self.inventory[0])
            self.remove(self.inventory[0])
            self.add(other.inventory[0])
            other.remove(other.inventory[0])
            return True
        else:
            return False