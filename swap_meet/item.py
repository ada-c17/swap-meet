class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        ratings = {
            0: "Quite used, but once super cute - could refactor it like bad code!",
            2: "It's been through a lot",
            1: "Verrry used, but quality fabric and fit",
            3: "Passable",
            4: "Mint condition, sparkly and all",
            5: "Nevern worn, labels and all, not like new -- it IS new!"
        }

        return ratings[self.condition]