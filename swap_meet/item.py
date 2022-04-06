class Item:

    CONDITION_RATINGS = {
    0: "You can help me throw in the trash",
    1: "Poor",
    2: "Fair",
    3: "Good Condition",
    4: "Mint",
    5: "Brand New"
    }

    def __init__(self, category="", condition=0, age=None):
        
        self.category = category
        self.condition = condition
        self.age = age


    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, new_condition):
        if 0 <= new_condition <= 5:
            self._condition = new_condition
        else:
            raise ValueError("Condition rating must be from 0 to 5.")
    
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age=None):
        if new_age is None or new_age > 0:
            self._age = new_age
        else:
            raise ValueError("Age must be larger than 0.")


    @staticmethod
    def __str__():
        return "Hello World!"
    

    def condition_description(self):
        return Item.CONDITION_RATINGS.get(int(self.condition), None)