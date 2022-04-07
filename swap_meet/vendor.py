from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self,new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self,new_item):
        try:
            self.inventory.remove(new_item)
            return new_item
        except ValueError as error:
            print(f"{new_item} not in inventory")
            return False

    def get_by_category(self,category):
        category_list = []
        try:
            for item in range(len(self.inventory)):
                if self.inventory[item].category == category:
                    category_list.append(self.inventory[item])
            # return category_list
        except ValueError as error:
            print(f"There are no {category} in inventory")
        return category_list

    def swap_items(self,Friend,my_item,their_item):
        index1 = 0
        index2 = 0
        if my_item not in self.inventory or their_item not in Friend.inventory:
            return False
        for x in range(len(self.inventory)):
            if self.inventory[x] == my_item:
                index1 = x
        for y in range(len(Friend.inventory)):
            if Friend.inventory[y] == their_item:
                index2 = y
        self.inventory[index1],Friend.inventory[index2] = Friend.inventory[index2],self.inventory[index1]
        print(f"Self {self.inventory}")
        print(f'Friend {Friend.inventory}')
        return True
    
    def swap_first_item(self,Friend):
        if len(self.inventory) < 1 or len(Friend.inventory) < 1:
            return False
        self.inventory[0],Friend.inventory[0] = Friend.inventory[0],self.inventory[0]
        return True

    def get_best_by_category(self,category):
        best_condition = 0
        counter = 0
        counter_category = 0
        for x in range(len(self.inventory)):
            if category  == self.inventory[x].category:
                counter_category += 1
        if counter_category == 0:
            return None
        for x in range(len(self.inventory)):
            if self.inventory[x].category == category:
                if self.inventory[x].condition > best_condition:
                    best_condition = self.inventory[x].condition
                    best_condition_index = x
        return self.inventory[best_condition_index]
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        my_swap = self.get_best_by_category(their_priority)
        their_swap = other.get_best_by_category(my_priority)
        if my_swap == False or their_swap == False:
            return False
        result = self.swap_items(other,my_swap,their_swap)
        print(self.inventory)
        print(other.inventory)
        return result

