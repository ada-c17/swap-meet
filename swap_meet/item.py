CONDITION_DESCRIPTION = {0:"One person's trash is another's treasure.",
1:"Probably not it's first swap meet.",
2:"Stained but functional",
3:"Used enough to know it works juuust right.",
4:"Stored for ages and finally seeing the light.",
5:"The tag is still on it."}

class Item:

    def __init__(self, category = "", condition = 0):
            self.category = category
            self.condition = condition


    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        for key, value in CONDITION_DESCRIPTION.items():
            if self.condition is key:
                return value
        