class Vendor:
    def __init__(self, inventory = None) :
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if category == item.category:
                item_list.append(item)

        return item_list

    def swap_items(self, vendor: 'Vendor', my_item, their_item):
        if my_item not in self.inventory:
            return False
        if their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, vendor: 'Vendor'):
        if not self.inventory or not vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = vendor.inventory[0]

        return self.swap_items(vendor, my_item, their_item)
        
    def get_best_by_category(self, category = ''):
        if not self.inventory:
            return None

        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        if not category_items:
            return None
    
        best_item = max(category_items, key=lambda item: item.condition)
        return best_item

    def swap_best_by_category(self, other: 'Vendor', my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_item, their_item)
