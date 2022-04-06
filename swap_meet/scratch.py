from item import Item

item = Item("bag")

string_return = item.__str__()

print(string_return)

print(repr(item))