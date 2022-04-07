from operator import attrgetter

class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else list() #using empty list constructor to explicitly note list data type expected

    def add(self, item):
        self.inventory.append(item) #appends instance of Item to inventory list
        return item
    
    def remove(self, item):
        if item not in self.inventory: #guard clause if item not in inventory
            return False
        
        self.inventory.remove(item) #removes instance of Item from inventory list
        return item
    
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category==category] #creates a list of all items in inventory whose category attribute matches category parameter
    
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory: #guard clause if either item not available to swap
            return False

        self.add(their_item)
        friend.add(my_item)
        self.remove(my_item)
        friend.remove(their_item)
        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory: #guard clause if either inventory is empty
            return False

        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return True
        
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if not items_in_category: #guard clause if category not available in inventory
            return None
        #accesses the values of the condition attribute in items_in_category and returns the item with the highest value
        return max(items_in_category, key=attrgetter('condition'))
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        self_items_in_category = self.get_by_category(their_priority)
        friend_items_in_category = other.get_by_category(my_priority)
        if not self_items_in_category or not friend_items_in_category: #guard clause if priority category not available in other inventory
            return False

        self_best_item = self.get_best_by_category(their_priority)
        friend_best_item = other.get_best_by_category(my_priority)
        self.swap_items(other, self_best_item, friend_best_item)
        return True

    #*********************************************************************
    ###Adding optional enhancements###
    #*********************************************************************
    def get_newest(self):
        if not self.inventory:
            return None
        return min(self.inventory, key=attrgetter('age'))

    def swap_by_newest(self, other):
        if not self.inventory or not other.inventory:
            return False

        self_newest = self.get_newest()
        friend_newest = other.get_newest()
        self.swap_items(other, self_newest, friend_newest)
        return True
    #*********************************************************************
    ###End optional enhancements###
    #*********************************************************************
