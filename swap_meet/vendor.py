# from .item import Item
class Vendor:
    def __init__(self, inventory = None):
        """
        You should not make the default parameter 
        a mutable objest. Set inventory as an 
        empty list.
            Parameters: inventory(list) = If no parameter passed in,
            inventory is an empty list
        """
        if not inventory:
            inventory = []
        self.inventory  = inventory
    
    def add(self, added_item):
        """
        Adds items to inventory list

            Parameters:
                    added_item(str): String of item added inventory(list)
            

            Returns:
                    added_item(str): String of item added inventory(list)
        """
        self.inventory.append(added_item)
        return added_item

    def remove(self, remove_item):
        """
        Checks to make sure remove_item is in inventory
        Removes items to inventory list

            Parameters:
                    remove_item(str): String of item remove inventory(list)
            

            Returns:
                    remove_item(str): String of item remove inventory(list)
        """
        if remove_item not in self.inventory:
            return False
        self.inventory.remove(remove_item)
        return remove_item

    def get_by_category(self, category):
        """
        Get category from inventory list

            Parameters: category(str): String used make to
                        compare to the category(str) in 
                        inventory(list)
            

            Returns:
                    category_items(list): Empty list
        """
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, friend, my_item, friend_item):
        """
        Remove items (my_item & friend_item) in each respective
        list (self.inventory & friend.inventory) and appends it 
        the other list
        (my_items to friend list and friend_items to my list)

            Parameters: friend(Vendor) = An instance
                        
                        my_item(str) = An instance of Item
                        
                        friend_item(str) = An instance of Item
            

            Returns:
                    False(bool): If my_item is NOT IN my inventory list 
                    or friend_item is NOT IN my friend's inventory list
                    
                    True(bool): If my_item IS IN my inventory list 
                    AND friend_item IS IN my friend's inventory list,
                    Exchange items
        """
        if my_item not in self.inventory or\
            friend_item not in friend.inventory:
            return False
        else:
            friend.inventory.append(my_item)
            self.inventory.append(friend_item)
            friend.inventory.remove(friend_item)
            self.inventory.remove(my_item)
            return True


    def swap_first_item(self, friend):
        """
        Envoke swap_items as helper method to remove first items in 
        each list (self.inventory & friend.inventory) and put at the 
        end of the other list (my inventory[first item]) to friend's 
        inventory[first item] and friend's inventory[first item] to 
        my inventory[first item])

            Parameters: friend(instance of Vendor class) = An instance 
                        of Vender class


            Returns:
                    False(bool): If one of the lists is empty
                    
                    True(bool): If both lists exists, Exchange items
        """
        if not self.inventory or\
            not friend.inventory:
            return False

        else:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True

    def get_best_by_category(self, category):
        if not category:
            return False
        best_condition = 0
        best_item = None
        items_in_category = self.get_by_category(category)
        for item in items_in_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        friend_item = other.get_best_by_category(my_priority) # Item I want to get from them
        my_item = self.get_best_by_category(their_priority) # Item I want to get from them
        if not friend_item or not my_item:
            return False
        return self.swap_items(other, my_item, friend_item)