from item import Item

class Vendor():
    # create inventory parameters, where deafalt is empty list
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    

    # create instance method add which add things in inventory list
    def add(self,item):
        self.inventory.append(item)
        return item


    # create instance method remove which remove item from inventory list
    def remove(self,item):
        for items in self.inventory:
            if item == items:
                self.inventory.remove(items)
                return items
        return False


    # create instance method which return a list of Items in the inventory with that category
    def get_by_category(self,category):
        list_of_items = []
        for item in self.inventory:
            if category == item.category:
                list_of_items.append(item)
        return list_of_items


    # create instance method implement swaping process
    def swap_items(self, friend, my_item, friends_item):
        
        if not my_item or not friends_item:
            return False
        
        else:
            if my_item in self.inventory and friends_item in friend.inventory:
                # vendor swap his item
                self.remove(my_item)
                friend.add(my_item)
                # friend swap his item
                friend.remove(friends_item)
                self.add(friends_item)
                return True

    # create instance method implement swaping process first item
    def swap_first_item(self, friend):

        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            # grab first element from self list: first_item = self.inventory[0]
            # remove from self inventory: self.remove(first_item)
            # add to friends inventory: friend.add(first_item)

            # grab first element from friends list: first_item = friend.inventory[0]
            # remove this elem from friensd list: friend.remove(first_item)
            # add to self inventory: self.add(first_item)
            return True


item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item(category="electronics")
item_e = Item(category="decor")
jolie = Vendor(
    inventory=[item_d, item_e]
)

# result = fatimah.swap_first_item(jolie)

print(jolie.first)
# print(item_a.category)
