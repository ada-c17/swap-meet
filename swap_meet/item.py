'''
Item class represents objects for trade at the swap meet, and instances of it make up the 'inventory' attribute for the Vendor class. 
Attributes include category (string), condition (float), and age(float), all optional.
Includes condition_description method which returns a string description associated with the numeric rating given for the item's condition.
'''


class Item:

    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        condition_descriptions = {
            0: "No condition provided",
            .5: "Not great",
            1: "Meh",
            1.5: "Existent",
            2: "Passable",
            2.5: "Okayish",
            3: "Decent",
            3.5: "Pretty good",
            4: "Great",
            4.5: "Like new",
            5: "Better than new"
        }
        return condition_descriptions[self.condition]
