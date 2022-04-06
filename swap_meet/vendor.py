
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


    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True
        
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        # elif self.inventory[0] not in friend.inventory:
        friend.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])            

        # if friend.inventory[0] not in self.inventory:
        self.inventory.append(friend.inventory[0])
        friend.inventory.remove(friend.inventory[0])

        return True

        
            
            
    

