class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item 


    def remove(self, item):
        if item not in self.inventory:
            return False 

        self.inventory.remove(item)
        return item 


    def get_by_category(self, category):
        categorized_list = []

        for item in self.inventory:
            if item.category == category:
                categorized_list.append(item)

        return categorized_list


    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False 

        friend.inventory.append(my_item)
        self.inventory.append(their_item)
        friend.inventory.remove(their_item)
        self.inventory.remove(my_item)

        return True


    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False 
        
        self_first = self.inventory[0]
        friend_first = friend.inventory[0]

        return self.swap_items(friend, self_first, friend_first)


    def get_best_by_category(self, category):
        best_category_condition = 0.0
        best_category_item = None

        for item in self.inventory:
            if item.category == category and item.condition > best_category_condition:
            # if item.category == category:
            #     if item.condition >= best_category_condition:
                    best_category_condition = item.condition
                    best_category_item = item
        
        return best_category_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        friend_swap = self.get_best_by_category(their_priority)
        self_swap = other.get_best_by_category(my_priority)

        if not friend_swap or not self_swap:
            return False

        return self.swap_items(other, friend_swap, self_swap)


    def swap_by_newest_helper(self):
        self_newest = self.inventory[0].age
        self_newest_item = self.inventory[0]

        for item in self.inventory:
            if item.age < self_newest:
                self_newest = item.age
                self_newest_item = item 
        
        return self_newest_item


    def swap_by_newest(self, other):
        """
        swap_by_newest() takes two parameters - self and other - and using
        the swap_by_newest_helper method finds the newest item, and then makes
        the swap using swap_items(). If there is more than 1 item with the
        same lowest age, it returns the first instance. 
        """
        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False 

        return self.swap_items(other, Vendor.swap_by_newest_helper(self), Vendor.swap_by_newest_helper(other))

