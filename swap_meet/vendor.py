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
        
        needs_to_add_to_self = friend.inventory.remove(their_item)
        needs_to_add_to_friend = self.inventory.remove(my_item)
        updated_self = self.inventory.append(needs_to_add_to_self)
        updated_friend = friend.inventory.append(needs_to_add_to_friend)

        return True