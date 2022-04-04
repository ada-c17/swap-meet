class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False

    def get_by_category(self, category):
        ''' input: string, representing a category. Output: list of Items in the inventory w/that category'''
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
            if items == []:
                return False
        return items
        
    # def swap_items(self, Vendor(friends_inventory), Item(my_item), Item(their_item)):
        pass
#     It removes the my_item from this Vendor's inventory, and adds it to the friend's inventory
# It removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
# It returns True
# If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, the method returns False
