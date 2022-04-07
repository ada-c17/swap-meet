class Item:
    def __init__(self, category = "", condition = 0, age = 1.0):
        self.category = category 
        self.condition = condition
        # if type(age) != float or type(age) != int:
        #     raise Exception("Age must be an int or float")
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0.0:
            return "Poor"
        elif self.condition == 1.0:
            return "Acceptable"
        elif self.condition == 2.0:
            return "Good" 
        elif self.condition == 3.0:
            return "Very Good" 
        elif self.condition == 4.0:
            return "Like New" 
        elif self.condition == 5.0:
            return "Brand New" 
        else: 
            return "Something went wrong"


    # blackbox testing - interact with methods/classes blind to how they work on the inside, give it weird inputs or test to see what it does from outsider's POV
    # clearbox testing - get to look at the code, see how it actually works, more in tune to where rough edges may lie