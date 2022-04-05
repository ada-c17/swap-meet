class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if inventory is None:
            self.inventory = []
       

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False

    def get_by_category(self, category):
        ''' input: string, representing a category. Output: list of Items in the inventory w/that category'''
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
            if items == []:
                return False
        return items

    #  result = fatimah.swap_items(jolie, item_b, item_d)
    # passing in instance of Vendor, instance of Item, instance of Item
    def swap_items(self, vendor_friend, my_item, their_item):
        '''
        input: 3 parameters: One instance of vendor class (a friend), two instances of item classes.
            The items will be swapped: first item will be added to current vendor, second item will be added to 2nd vendor
            ouptut: True or False (False if items that should be swapped are not within their vendor's inventory)
        '''
        if my_item in self.inventory and their_item in vendor_friend.inventory:
            #vendor_friend.inventory.append(my_item)
            vendor_friend.add(my_item)
            #self.inventory.remove(my_item)
            self.remove(my_item)
            #self.inventory.append(their_item)
            self.add(their_item)
            #vendor_friend.inventory.remove(their_item)
            vendor_friend.remove(their_item)
            return True
        else: 
            return False

# Here, both instances are called into the function:

# def test_get_student_with_more_classes_student_a():
#     charles = Student("Charles Babbage", "senior", ["mechanical engineering"])
#     ada = Student(
#         "Ada Lovelace",
#         "sophomore",
#         ["mathematics", "foundations of computing"]
#     )
#     # act
#     student_a = charles.get_student_with_more_classes(ada, charles)
#     assert student_a == ada    

# def get_student_with_more_classes(self, student_a, student_b):
#         if student_a.get_num_classes() > student_b.get_num_classes():
#             return student_a
#         return student_b
