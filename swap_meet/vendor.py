#from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
           inventory = []
        self.inventory = inventory

    def add(self, item):
        if not item:
            return False

        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        #list_of_items_per_cat = []  # do i need .self? i do not.

        # for item in self.inventory:
        #     if item.category == category:
        #        list_of_items_per_cat.append(item)

        # list comprehension
        list_of_items_per_cat = [item for item in self.inventory if item.category == category]

        return list_of_items_per_cat

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        '''
        order does not matter
        self.inventory.remove or other_vendor.remove does not matter
        self.other_vendor / self.my_item, etc. does not matter
        '''
        other_vendor.add(my_item)
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        self.add(other_vendor.inventory[0])
        other_vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        other_vendor.remove(other_vendor.inventory[0])

        return True

    def get_best_by_category(self, category):

        items_by_cat = self.get_by_category(category)

        if len(items_by_cat) == 0:
            return None

        best_item = items_by_cat[0]
        for item in items_by_cat:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item_other = other.get_best_by_category(my_priority)
        best_item_mine = self.get_best_by_category(their_priority)

        if not best_item_other or not best_item_mine:
            return False

        self.swap_items(other, best_item_mine, best_item_other)

        return True


rafferty = Vendor()
closet_items = ["white shirt", "balenciaga jeans", "flat shoes", "work gown"]
rafferty.inventory = closet_items
# print(vars(rafferty))
rafferty.add("elegant work gown")
rafferty.remove("flat shoes")
# print(vars(rafferty))
oriana = Vendor()
closet_items2 = ["yellow shirt", "method jeans", "ballet flats", "red jacket"]
oriana.inventory = closet_items2
print(vars(rafferty))
rafferty.swap_items(oriana, rafferty.inventory[0], oriana.inventory[0])
print(vars(rafferty))


'''
Notes and Questions:


# questions

'''
