class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        cond_dict = {
            0: "OMG, that's really bad!!",
            1: "It can only go up from here",
            2: "You might want to work on this one a bit", 
            3: "Just average",
            4: "Pretty darn good!",
            5: "Woah!! This is stellar!"
            }

        verbiage = cond_dict[self.condition]
        return verbiage
        