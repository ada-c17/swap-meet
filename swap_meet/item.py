#from swap_meet.vendor import Vendor

class Item:
    def __init__(self,category="",condition=0,age=0):
        self.category = category
        self.condition = condition
        self.age = age
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition = {
            1:"poor",
            2:"fair",
            3:"good",
            4:"like new",
            5:"brand new"  
        }
        return f"condition is {condition[self.condition]}" 
        

        

    
        
        

        

        