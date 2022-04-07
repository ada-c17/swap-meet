from operator import attrgetter
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory =None):
        if inventory is None:
            inventory =[]
        # if isinstance(inventory,list) and not inventory:
        self.inventory = inventory
        # elif all(isinstance(x, Item) for x in inventory):   
        #     self.inventory = inventory
        # else:
        #     raise ValueError ("Argument inventory should be a list of objects class Item")  
        # ! I cant add the logic above because tests in Wave1 pass the list of strings!
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            indx=self.inventory.index(item)
            item_removed=self.inventory.pop(indx)   
        else:
            return False
        return item_removed    

    def get_by_category(self, category):
        return [i for i in self.inventory if i.category ==category]  

    def swap_items(self, friend,my_item, their_item ):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        friend.remove(their_item)
        friend.add(my_item)
        return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory ==[]:
            return False
        my_item =self.inventory[0]    
        their_item=friend.inventory[0]
        self.swap_items(friend,my_item, their_item)
        return True

    #* below are two functions for Wave 6
    # def get_best_by_category(self, category):
    #     matching_category=self.get_by_category(category)
    #     return max(matching_category, key =attrgetter('condition'), default=None)

    # def swap_best_by_category(self,other,my_priority, their_priority):
    #     my_best_item=self.get_best_by_category(their_priority)
    #     their_best_item=other.get_best_by_category(my_priority)
    #     if my_best_item is None or their_best_item is None:
    #         return False
    #     self.swap_items(other, my_best_item, their_best_item)
    #     return True


    #* I know, that I used decorators in an unusual way, because when I started to implement them, I did not fully understand them and I thought we use decorators to change the behaviour of the function. Now I learned that decorators should not change but extend the behaviour of the function. However because they work and I learned through this exersize a lot - I decided to leave the code as it is. I learned my lesson and promise not to use decorators for changing the behavior of the function again. Below in comments you can find a correct way to implement my idea that Matt McKnett recommendended.
    #  
    # f_max_min ={ 'age': min,'condition':max}

    # def attr_decorator(attr):
    #     def a_decorator_passing_arguments(method_to_decorate):
    #             def a_wrapper_accepting_arg(self, category):
    #                 matching_category=self.get_by_category(category)
    #                 return  self.f_max_min[attr](matching_category, key =attrgetter(attr), default=None)
    #             return a_wrapper_accepting_arg
    #     return a_decorator_passing_arguments          

    # @attr_decorator(attr='condition')
    # def get_best_by_category(self, category):
    #     pass
    
    # @attr_decorator(attr='age')
    # def get_best_by_age(self, category):
    #     pass
    
    # funcs={ 'age': get_best_by_age,
    #         'condition':get_best_by_category}

    # def attr_decorator(attr):
    #     def a_decorator_passing_arguments(method_to_decorate):           
    #         def a_wrapper_accepting_arg(self,other,my_priority, their_priority):
    #                 my_best_item=self.funcs[attr](self, their_priority)
    #                 their_best_item=other.funcs[attr](other, my_priority)
    #                 if my_best_item is None or their_best_item is None:
    #                     return False
    #                 self.swap_items(other, my_best_item, their_best_item)
    #                 return True         
    #         return a_wrapper_accepting_arg
    #     return a_decorator_passing_arguments        

    # @attr_decorator(attr='condition')
    # def swap_best_by_category(self,other,my_priority, their_priority):
    #     return True

    # @attr_decorator(attr='age')
    # def swap_by_newest(self,other,my_priority, their_priority):
    #     return True    

    #* the code above should be refactored to this:

    # f_max_min ={'age': min,'condition':max}

    # def get_best_by_attr(self, category, attr):
    #     matching_category=self.get_by_category(category)
    #     res = self.f_max_min[attr](matching_category, key =attrgetter(attr), default=None)
    #     return res         

    # def get_best_by_category(self, category):
    #     return self.get_best_by_attr(category, 'condition')
    
    # def get_best_by_age(self, category):
    #     return self.get_best_by_attr(category, 'age')


    # me again. Day3. Learning closures. another way to implement the code. maybe not the best way, but its cool that there are so many different ways to achive the same goal. 

    f_max_min ={ 'age': min,'condition':max}
    def using_closures(attr):                               
        def get_best_by(self, category):
            matching_category=self.get_by_category(category)
            return  self.f_max_min[attr](matching_category, key =attrgetter(attr), default=None)
        return get_best_by
    get_best_by_category=using_closures('condition')    
    get_best_by_age=using_closures('age')
    
    
    funcs={ 'age': get_best_by_age,
            'condition':get_best_by_category}

    def using_closures2(attr):
        def swap_best_by(self,other,my_priority, their_priority):
            my_best_item=self.funcs[attr](self, their_priority)
            their_best_item=other.funcs[attr](other, my_priority)
            if my_best_item is None or their_best_item is None:
                    return False
            self.swap_items(other, my_best_item, their_best_item)
            return True         
        return swap_best_by

    swap_best_by_category=using_closures2('condition')  
    swap_by_newest=using_closures2('age')