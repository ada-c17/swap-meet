from swap_meet.utils import CONDITION_RATINGS


class Item:

    def __init__(self, category="", condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age

    @staticmethod
    def __str__():
        return "Hello World!"
    
    def condition_description(self):
        return CONDITION_RATINGS.get(self.condition, None)