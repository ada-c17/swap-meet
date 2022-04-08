from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        #code on lines 6-7 from https://docs.python-guide.org/writing/gotchas/
        if inventory == None:
            inventory = []
        self.inventory = inventory

    # Adds the item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item


    # Removes the matching item from the inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item


    # Takes one argument: a string, representing a category
    # Returns a list of Items in the inventory with that category
    def get_by_category(self, category):
        #self.item = Item(category)
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)


        return item_list


    # removes my_item from this Vendor's inventory
    # adds my_item to the other Vendor's inventory
    # removes their_item from other Vendor's inventory
    # adds their_item to the this Vendor's inventory
    def swap_items(self, other_vendor, my_item, their_item):

        if (my_item not in self.inventory) or (their_item not in other_vendor.inventory):
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        
        other_vendor.remove(their_item)
        self.add(their_item)
        

        return True


    #removes first item from this Vendor's inventory
    # adds the other Vendor's first item
    # removes first item from other Vendor's inventory
    # adds this Vendor's first item
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return True


    #gets the item with the best condition in a certain category
    def get_best_by_category(self, category):

        category_inventory = self.get_by_category(category)

        if len(category_inventory) == 0:
            return None
        
        highest_rated = category_inventory[0]
        
        for item in category_inventory:
    
            if (item.condition) > (highest_rated.condition):
                highest_rated = item
                
        return highest_rated


    #swap the best item of certain categories with another Vendor 
    def swap_best_by_category(self, other, my_priority, their_priority):

        #find best item in my inventory that matches their_priority
        my_best = self.get_best_by_category(their_priority)

        their_best = other.get_best_by_category(my_priority)
        
        if my_best == None or their_best == None:
            return False

        self.swap_items(other, my_best, their_best)

        return True

        

    def swap_by_newest(self, other):
        my_newest = self.inventory[0]
        for item in self.inventory:
            if not item.age is None:
                my_newest = item
                break
        if my_newest.age is None:
            return False
        
        for item in self.inventory:
            if not item.age is None:
                if item.age < my_newest.age:
                    my_newest = item

        their_newest = other.inventory[0]
        for item in other.inventory:
            if not item.age is None:
                their_newest = item
                break
        if their_newest.age is None:
            return False
        
        for item in other.inventory:
            if not item.age is None:
                if item.age < their_newest.age:
                    their_newest = item

        self.swap_items(other, my_newest, their_newest)
        return True







