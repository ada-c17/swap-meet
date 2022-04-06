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
            if item.category == category:
                if item.condition >= best_category_condition:
                    best_category_condition = item.condition
                    best_category_item = item
        
        return best_category_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        friend_swap = self.get_best_by_category(their_priority)
        self_swap = other.get_best_by_category(my_priority)

        if not friend_swap or not self_swap:
            return False

        return self.swap_items(other, friend_swap, self_swap)


    def swap_by_newest(self, other):
        """
        swap_by_newest() takes two parameters - self and other - and
        finds the newest item, and then makes the swap using swap_items()
        """

        self_newest = 100000
        self_newest_item = None
        friend_newest = 100000
        friend_newest_item = None

        for item in self.inventory:
            if item.age < self_newest:
                self_newest = item.age
                self_newest_item = item 
        
        for item in other.inventory:
            if item.age < friend_newest:
                friend_newest = item.age
                friend_newest_item = item
        
        return self.swap_items(other, self_newest_item, friend_newest_item)


