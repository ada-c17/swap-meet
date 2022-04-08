import pytest
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