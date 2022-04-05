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
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
        # Alternate method below - which one is better / closer to best practice?
        # if item in self.inventory:
        #     self.inventory.remove(item)
        #     return item
        # else:
        #     return False
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            # Leaving alternate ordering here because I have a question
            # Confused why when executing in this order, swap_first_item function still works
            # self.inventory.remove(my_item)
            # self.inventory.append(their_item)
            # other.inventory.remove(their_item)
            # other.inventory.append(my_item)
            self.inventory.append(their_item)
            other.inventory.append(my_item)
            self.inventory.remove(my_item)
            other.inventory.remove(their_item)
            return True

    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        else:
            self.swap_items(other, self.inventory[0], other.inventory[0])
            # Why does this work even though we are mutating list ordering mid function?
            return True

    def get_best_by_category(self, category):
        items_list = [item for item in self.inventory if item.category == category]
        if items_list == []:
            return None
        best_item = items_list[0]
        for item in items_list:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item_for_me = other.get_best_by_category(my_priority)
        best_item_for_them = self.get_best_by_category(their_priority)
        if best_item_for_me is None or best_item_for_them is None:
            return False
        else:
            self.swap_items(other, best_item_for_them, best_item_for_me)
            return True
        

