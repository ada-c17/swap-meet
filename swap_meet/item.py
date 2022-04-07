from datetime import date
class Item:
    #the decorated function below was not nesessary I just wanted to implement it
    @classmethod
    def __check_value(cls,x):
        return type(x) in (int, float)

    def __init__(self, category="", condition=0, age=date(2021,1,1)):
        self.category=''
        self.condition=0
        self.age=1
        if isinstance(category, str) and self.__check_value(condition) and isinstance(age, date):
            if condition>5: condition=5
            if condition<0:condition=0
            self.condition =int(condition)
            self.category =category
            today=date.today()
            if age>today: age=today
            self.age= today.year-age.year
        else:  
            raise ValueError ("First argument is a string type, second argument is number, third argument is a date")     

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

