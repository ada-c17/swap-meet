

class Item():
    def __init__(self, category=None, condition=0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
        return("Hello World!")

    def condition_description(self):
        if self.condition <= 1:
            return("absolutly horrendous")
        elif self.condition <= 2:
            return("kinda horrendous")
        elif self.condition <= 3:
            return("its mid")
        elif self.condition <= 4:
            return("kinda perfect")
        elif self.condition <= 5:
            return("absoluety perfect")

    # def get_by_category(self, category):
    #     variety = []
    #     invo = Vendor()
    #     for item in invo.self.inventory:
    #         if category == item:
    #             variety.append(item)
    #     return variety

        #     if category =asdd= item:
        #         variety.append(item)
        # return variety
