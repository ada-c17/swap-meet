
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
    
    
    def add(self, item):
        self.inventory.append(item)

        # print(f"This is the updated inventory: {updated_list}")
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
  
        return item

    def get_by_category(self, category):
        if not category:
            return False

        category_list = []
        for item in self.inventory:
            if item.category == category:

                category_list.append(item)
            
        return category_list

vendor_2 = Vendor("Vendor_2")

    def swap_items(self, ):
        
