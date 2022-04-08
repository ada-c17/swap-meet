class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory    

    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        
        if item in self.inventory:
            self.inventory.remove(item)
            
            return item
        else:
            return False

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, other_vendor, my_item, their_item):
        if not (my_item in self.inventory and their_item in other_vendor.inventory):
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        
        tmp = self.inventory[0]
        self.inventory[0] = other_vendor.inventory[0]
        other_vendor.inventory[0] = tmp

        return True

    def get_best_by_category(self, category):
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if best_item is None or item.condition > best_item.condition:
                    best_item = item
        return best_item
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item1 = self.get_best_by_category(their_priority)
        print(best_item1)
        best_item2 = other.get_best_by_category(my_priority)

        return self.swap_items(other, best_item1, best_item2)
        






        

           



