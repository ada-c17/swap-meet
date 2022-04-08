import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_adding_to_inventory_takes_multiple_items():
    vendor = Vendor()
    item_collection = [Clothing(),Decor(),Electronics()]

    vendor.add(item_collection)

    assert len(vendor.inventory) == 3

def test_adding_to_inventory_raises_error_w_dict():
    vendor = Vendor()
    item_collection = {'item_a':Clothing(),'item_b':Decor(),'item_c':Electronics()}

    with pytest.raises(ValueError):
        vendor.add(item_collection)

def test_removing_from_inventory_takes_multiple_items():
    a, b, c = Clothing(), Decor(), Electronics()
    vendor = Vendor([a, b, c])

    vendor.remove((a,c))

    assert len(vendor.inventory) == 1
    assert vendor.inventory[0] == b

def test_removing_from_inventory_raises_error_w_dict():
    a, b, c = Clothing(), Decor(), Electronics()
    vendor = Vendor([a, b, c])

    dict_to_remove = {'item_a': a,'item_c': c}

    with pytest.raises(ValueError):
        vendor.remove(dict_to_remove)

def test_adding_to_inventory_does_not_add_duplicates():
    a, b, c = Clothing(), Decor(), Electronics()
    vendor = Vendor([a, b])

    vendor.add([b, c])

    assert len(vendor.inventory) == 3

def test_when_removing_multiple_items_no_action_taken_if_any_item_not_found():
    a, b, c = Clothing(), Decor(), Electronics()
    vendor = Vendor([a, b])

    result = vendor.remove((a,c))

    assert len(vendor.inventory) == 2
    assert a in vendor.inventory
    assert result == False

def test_items_have_complete_descriptions_that_are_different_for_each_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    
    descriptions = [item.complete_description() for item in items]

    assert len(descriptions) == 3
    assert (descriptions[0] != descriptions[1]
            and descriptions[1] != descriptions[2]
            and descriptions[0] != descriptions[2])

def test_basic_items_have_complete_descriptions_with_no_category():
    basic_item_full_description = Item().complete_description()
    
    assert type(basic_item_full_description) is str
    assert len(basic_item_full_description) > 0

def test_items_have_condition_descriptions_for_all_values():
    
    descriptions = [Item(condition=(x/10)).condition_description() is not None for x in range(0,101)]

    assert len(descriptions) == 101
    assert all(descriptions)