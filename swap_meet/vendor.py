class Vendor():
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    

    '''Instance method add, which add itens in the inventory list'''
    def add(self,item):
        self.inventory.append(item)
        return item


    '''Instance method remove which remove item from inventory list'''
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    '''Instance method which return a list of items in the inventory with that category'''
    def get_by_category(self,category):
        list_of_items = []
        for item in self.inventory:
            if category == item.category:
                list_of_items.append(item)
        return list_of_items


    '''Instance method implement swaping process between vendor and other person'''
    def swap_items(self, friend, my_item, friends_item):
        if my_item in self.inventory and friends_item in friend.inventory:
            # vendor swap his item
            self.remove(my_item)
            friend.add(my_item)
            # friend swap his item
            friend.remove(friends_item)
            self.add(friends_item)
            return True
        return False


    '''Instance method implement swaping process first item'''
    def swap_first_item(self, friend):
        if len(self.inventory) and len(friend.inventory) != 0:
            self.swap_items(friend,self.inventory[0],friend.inventory[0])
            return True
        return False


    '''Instance method will get the item with the best condition in a certain category'''
    def get_best_by_category(self, consider_category):
        best_dict_category = {}
        best_dict_category[consider_category] = 0.0
        # creating counter to check no matches categories in vendors inventory
        count = 0
        # consider given represents string of category, add to dictionary 
        # matching category is key and value is rate. Setup first element
        # of dictionary like max and matching other rate, if higher add to dict 
        for category_from_inv in self.inventory:
            if consider_category == category_from_inv.category:
                count += 1
                if category_from_inv.condition > best_dict_category[consider_category]:
                    best_dict_category[category_from_inv.category] = category_from_inv.condition
                    best_category = category_from_inv
            if count == 0:
                return None
        return best_category

    '''Instance method will swap the item with the best condition in a certain category'''
    def swap_best_by_category(self, other, my_priority, their_priority):
        if len(self.inventory) and len(other.inventory) != 0:
            best_item_for_friend = self.get_best_by_category(their_priority)
            best_item_for_vendor = other.get_best_by_category(my_priority)
            if best_item_for_friend is None or best_item_for_vendor is None:
                return False
            else:
                self.swap_items(other,best_item_for_friend,best_item_for_vendor)
                return True
        return False
