class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self,category):
        return [item for item in self.inventory if item.category == category]

    def get_by_age(self):
        min_age = float("inf")
        min_items = [None]
        for item in self.inventory:
            if item.age < min_age:
                min_items[0], min_age = item, item.age
            if item.age == min_age:
                min_items.append(item)
        return min_items
    
    def swap_items(self,other,my_item,their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other.inventory.remove(their_item)
        other.inventory.append(my_item)
        return True

    def swap_first_item(self,other):
        if self.inventory == [] or other.inventory == []:
            return False
        my_item = self.inventory[0]
        their_item = other.inventory[0]
        # self.swap_items(other,my_item,their_item)
        self.inventory.append(their_item)
        other.inventory.append(my_item)
        del self.inventory[0] # O(1) vs O(n) in swap_items as we know the index
        del other.inventory[0] # O(1) vs O(n) in swap_items as we know the index
        return True

    def get_best(self,items_list):
        max_condition = 0
        max_item = None
        for item in items_list:
            if item.condition > max_condition:
                max_item, max_condition = item, item.condition
        return max_item

    def get_best_by_category(self,category):
        category_items = self.get_by_category(category)
        return self.get_best(category_items)
        
    def swap_best_by_category(self,other,my_priority,their_priority):
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)
        if their_item and my_item:
            self.swap_items(other,my_item,their_item)
            return True
        return False

    def swap_by_newest(self,other,best=False):
        their_items = other.get_by_age()
        my_items = self.get_by_age()
        if best:
            their_items[0] = self.get_best(their_items)
            my_items[0] = self.get_best(my_items)
        if their_items[0] and my_items[0]:
            self.swap_items(other,my_items[0],their_items[0])
            return True
        return False





