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
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, vendor_to_swap_with, self_item, their_item):
        if self_item in self.inventory and their_item in vendor_to_swap_with.inventory:
            self.inventory.remove(self_item)
            vendor_to_swap_with.inventory.append(self_item)
            self.inventory.append(their_item)
            vendor_to_swap_with.inventory.remove(their_item)
            return True
        else:
            return False

    def swap_first_item(self, vendor_to_swap_with):
        if len(self.inventory) >= 1 and len(vendor_to_swap_with.inventory) >= 1:
            self_item = self.inventory[0]
            their_item = vendor_to_swap_with.inventory[0]
            self.swap_items(vendor_to_swap_with, self_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self,category):
        items_in_category = self.get_by_category(category)
        if len(items_in_category) > 0:
            items_in_category.sort(key=lambda item: item.condition, reverse=True)
            return items_in_category[0]
        return None
