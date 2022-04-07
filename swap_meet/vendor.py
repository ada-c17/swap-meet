from operator import attrgetter

class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        # Add item to the inventory
        self.inventory.append(item)
        # Return item that was added to inventory
        return item
        

    def remove(self, item):
        # Check if item in inventory that are match
        if item in self.inventory:
            # Remove item from the inventory
            self.inventory.remove(item)
            return item
        return False # If no matching items

    def get_by_category(self, category):
        # Return a list of item inventory from that category
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):

        # Check if Vendor items not in her inventory or Vendor friend's item not in their inventory
        if not my_item in self.inventory or not their_item in other.inventory:
            return False
        
        # Vendor(my_item) add friend items to her inventory
        self.inventory.append(their_item)
        # Vendor remove her own items from her inventory
        self.inventory.remove(my_item)
        # Vendor friend's add Vendor to their inventory
        other.inventory.append(my_item)
        # Vendor friend's remove their item from their inventory
        other.inventory.remove(their_item)

        return True # Return True when Vendor and Vendor friend's swaping items from each other inventory

    def swap_first_item(self, other):
        # Check if Vendor and Vendor friend's inventory is not empty
        if self.inventory and other.inventory:
            # using index to access first item from vendor inventory
            my_item = self.inventory[0]
            #using index to access first item from vendor friend's inventory
            their_item = other.inventory[0]
            # using helper function, to swap first item from vendor and vendor friend's inventory
            self.swap_items(other, my_item, their_item)

            return True

        return False # If empty list return False

    def get_best_by_category(self, category):
        # Check if there is no items in the inventory that match category
        if not self.get_by_category(category):
            return None
        # Return the item that are match category and highest condition even there's duplicate items
        return max(self.get_by_category(category), key=attrgetter("condition"))

    def swap_best_by_category(self, other, my_priority, their_priority):
        # Find the best items in Vendor inventory to match their priority
        my_best_item = self.get_best_by_category(their_priority) 
        # Find the best items in Vendor friend's to match Vendor priority
        their_best_item = other.get_best_by_category(my_priority)
        
        # Return swap best items between Vendor and Vendor friend's from inventory
        return self.swap_items(other, my_best_item, their_best_item)
        
    
    def swap_by_newest(self):
        # Set minimum ages to float infinity
        new_ages = float("inf")
        # Set minimum items to None list
        items = [None]
        # Iterate item in the inventory
        for item in self.inventory:
            # Check if the item age is less than the new ages
            if item.age < new_ages:
                # update the item age 
                items[0], new_ages = item, item.age
            else:
                # if item age equal to new age
                if item.age == new_ages:
                    # Add item to items list
                    items.append(item)
        return items
    
    

