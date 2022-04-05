#from swap_meet.vendor import Vendor

class Item:
    def __init__(self,category="",condition=0):
        self.category=category
        self.condition=condition

    def __str__(self):
        return (f"Hello World!")   

    def condition_description(self): 
        cond_description=self.condition
        if cond_description==0:
            return ("very bad")
        elif cond_description==1:
            return("moderate")
        elif cond_description==2:
            return("normal")
        elif cond_description==3:
            return("acceptable")    
        elif cond_description==4:
            return ("good")

        return ("very very good")    



