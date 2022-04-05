class Item:
    @classmethod
    def __check_value(cls,x):
        return type(x) in (int, float)

    def __init__(self, category="", condition=0, age =0):
        self.category=''
        self.condition=self.age=0
        if isinstance(category, str) and self.__check_value(condition) and self.__check_value(age):
            self.condition =condition
            self.category =category
            self.age=age
        else:  
            raise ValueError ("First argument is a string type, second and third arguments are numbers")     

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_int=int(self.condition)
        description={
            0:"You probably want a glove for this one...",
            1:"poor",
            2:"fair",
            3:"good",
            4:"like new",
            5:"new"
        }    
        return description[condition_int]

