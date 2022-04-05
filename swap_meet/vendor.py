class Vendor:
    def __init__(self, inventory = []):
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

        if len(categorized_list) >= 1:
            return categorized_list
        else: 
            return None 

        # categorized_list if len(categorized_list) >= 1 else None 

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

        self.inventory.append(friend_first)
        friend.inventory.append(self_first)
        self.inventory.remove(self_first)
        friend.inventory.remove(friend_first)

        return True 

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

        self.inventory.append(self_swap)
        other.inventory.append(friend_swap)
        self.inventory.remove(friend_swap)
        other.inventory.remove(self_swap)

        return True

