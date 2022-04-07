import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_age_attribute():
    item = Clothing(condition = 2.0, age = 2)
    assert item.age == 2

def test_get_newest_item_empty_inventory_is_False():
    tai = Vendor(inventory=[])

    result = tai.get_newest_item()

    assert result == False

def test_get_newest_item():
    item_a = Clothing(condition=2.0, age = 4)
    item_b = Decor(condition=4.0, age = 2)
    item_c = Clothing(condition=4.0, age = 1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.get_newest_item()

    assert result == item_c    

def test_swap_by_newest_is_false_with_no_inventory():
    item_a = Clothing(condition=2.0, age = 4)
    item_b = Clothing(condition=4.0, age = 2)
    tai = Vendor(inventory=[item_a, item_b])

    jesse = Vendor(inventory=[])
    
    result = tai.swap_by_newest(jesse)

    assert result == False

def test_no_age_returns_value_error():
    item_a = Clothing(condition=2.0, age = 4)
    item_b = Clothing(condition=4.0)
    tai = Vendor(inventory=[item_a, item_b])

    item_c = Clothing(condition=2.0, age=4)
    jesse = Vendor(item_c)
    
    with pytest.raises(ValueError):
        result = tai.swap_by_newest(jesse)

def test_swap_by_newest():
    item_a = Clothing(condition=2.0, age = 4)
    item_b = Decor(condition=4.0, age = 2)
    item_c = Clothing(condition=4.0, age = 1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )


    item_d = Clothing(condition=2.0, age = 4)
    item_e = Decor(condition=4.0, age = 2)
    item_f = Clothing(condition=4.0, age = 1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(
        other=jesse,
    )

    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_f]
    assert jesse.inventory == [item_d, item_e, item_c]