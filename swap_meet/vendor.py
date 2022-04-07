class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
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

    def get_by_category(self, category):
        items_by_category = [item for item in self.inventory if item.category == category]
        return items_by_category

    def swap_items(self, other, yours, theirs):
        if yours in set(self.inventory) and theirs in set(other.inventory):
            other.add(yours)
            self.remove(yours)
            self.add(theirs)
            other.remove(theirs)
            return True

    def swap_first_item(self, other):
        try:
            yours = self.inventory[0]   
            theirs = other.inventory[0]
            other.add(yours)
            self.add(theirs)
            self.remove(yours)
            other.remove(theirs)
            return True
        except IndexError:
            return False

    def get_best_by_category(self, category):
        try:
            category_list = self.get_by_category(category)
            best = max(category_list, key=lambda x: x.condition)
            return best

        except ValueError:
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        theirs = other.get_best_by_category(my_priority)
        yours = self.get_best_by_category(their_priority)
        if theirs and yours:
            other.add(yours)
            self.add(theirs)
            self.remove(yours)
            other.remove(theirs)
            return True

    def get_newest(self):
        newest = min(self.inventory, key=lambda x: x.age)
        return newest

    def swap_by_newest(self, other):
        theirs = other.get_newest()
        yours = self.get_newest()
        other.add(yours)
        self.add(theirs)
        other.remove(theirs)
        self.remove(yours)
        return True