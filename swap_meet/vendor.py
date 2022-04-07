class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    
    def get_by_category(self, category1):
        category_list = []
        for item in self.inventory:
            if category1 == item.category:
                category_list.append(item) #Item(category="clothing")
        return category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            exchange_item = self.remove(my_item)
            friend.add(exchange_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False


    def swap_first_item(self,vendor_friend):
        if not self.inventory or not vendor_friend.inventory:
            return False

        my_first_item = self.inventory.pop(0)
        vendor_friend.add(my_first_item)
        friend_first_item = vendor_friend.inventory.pop(0)
        self.add(friend_first_item)

        return True

    def get_best_by_category(self, category):
        '''get the item with the best condition
        in a certain category'''
    
        category_best = self.get_by_category(category)
        if not category_best:
            return None

        current_max = category_best[0]
        for item in category_best:
            if item.condition > current_max.condition:
                current_max = item
        return current_max
        

    def swap_best_by_category(self, other, my_priority, their_priority):
        ''' swap the best item of certain categories with another Vendor'''
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False

        return self.swap_items(other, my_best, their_best)

        #OTHER-OPTION
        # if my_best and their_best:
        #     self.swap_items(other, my_best, their_best)
        #     return True
        # return False

        














