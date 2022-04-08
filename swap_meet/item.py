class Item:
    '''
    Item is the parent class to the Clothing, Decor, and Electronics classes, which inherit
    Item's attributes and methods. Instances of the Vendor class (vendors) can have
    Item class elements as elements of their inventories.

    The Item class' method condition_description returns a label (string) based on what
    value is passed onto its attribute condition.
    '''

    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        ratings = {
            0: "Quite used, but once super cute - could refactor it like bad code!",
            1: "It's been through a lot",
            2: "Verrry used, but quality fabric and fit",
            3: "Passable",
            4: "Mint condition, sparkly and all",
            5: "Nevern worn, labels and all, not like new -- it IS new!"
        }

        return ratings[self.condition]