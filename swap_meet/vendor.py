# from .item import Item
class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory  = inventory
    
    def add(self, added_item):
        self.inventory.append(added_item)
        return added_item

    def remove(self, remove_item):
        if remove_item not in self.inventory:
            return False
        self.inventory.remove(remove_item)
        return remove_item

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, friend, my_item, friend_item):
        if my_item not in self.inventory or\
            friend_item not in friend.inventory:
            return False
        elif my_item in self.inventory or\
            friend_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.append(friend_item)
            friend.inventory.remove(friend_item)
            self.inventory.remove(my_item)
            return True


    def swap_first_item(self, friend):
        if not self.inventory or\
            not friend.inventory:
            return False

        else:
            friend.inventory.append(self.inventory[0])
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            self.inventory.remove(self.inventory[0])
            return True

    def get_best_by_category(self, category):
        for item in self.inventory:
            print(f"*^*^*^*^{self.inventory =}*^*^*^*^")
            # if self.get_by_category() != category or\