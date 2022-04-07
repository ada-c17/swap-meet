import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

def test_get_newest_item_returns_correct_item_with_ages():
# Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Clothing(age=5)
    item_d = Item(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    # Act
    result = tai.get_newest_item()

    assert result
    assert len(tai.inventory) == 4
    assert tai.inventory == [item_a, item_b, item_c, item_d]
    assert result == item_a

def test_get_newest_item_returns_None_with_None_age():
# Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Clothing(age=5)
    item_d = Item(age=None)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    # Act
    result = tai.get_newest_item()

    assert not result
    assert len(tai.inventory) == 4
    assert tai.inventory == [item_a, item_b, item_c, item_d]
    assert result == None

def test_get_newest_item_returns_correct_item_with_float_ages():
# Arrange
    # me
    item_a = Decor(age=2.5)
    item_b = Electronics(age=4.2)
    item_c = Clothing(age=0.5)
    item_d = Item(age=3.6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    # Act
    result = tai.get_newest_item()

    assert result
    assert len(tai.inventory) == 4
    assert tai.inventory == [item_a, item_b, item_c, item_d]
    assert result == item_c

def test_get_newest_item_returns_None_with_empty_inventory():
    tai = Vendor()

    # Act
    result = tai.get_newest_item()

    assert not result
    assert len(tai.inventory) == 0
    assert result == None

def test_swap_by_newest_returns_False_with_my_item_as_None():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=4.2)
    item_c = Clothing(None)
    item_d = Item(age=3.6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Clothing()
    item_f = Decor()
    item_g = Clothing()
    jesse = Vendor(
        inventory=[item_e, item_f, item_g]
    )

    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 4
    assert jesse.inventory == [item_e, item_f, item_g]
    assert tai.inventory == [item_a, item_b, item_c, item_d]
    

def test_swap_by_newest_returns_False_with_my_item_as_None():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=4.2)
    item_c = Clothing(None)
    item_d = Item(age=3.6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    jesse = Vendor()

    result = tai.swap_by_newest(jesse)

    assert not result
    assert len(jesse.inventory) == 0
    assert len(tai.inventory) == 4
    assert jesse.inventory == []
    assert tai.inventory == [item_a, item_b, item_c, item_d]

def test_swap_by_newest_correctly_swaps_items():
    item_a = Decor(age=2.5)
    item_b = Electronics(age=4.2)
    item_c = Clothing(age=1)
    item_d = Item(age=3.6)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    item_e = Clothing(age=0.6)
    item_f = Decor(age=5)
    item_g = Clothing(age=7)
    jesse = Vendor(
        inventory=[item_e, item_f, item_g]
    )

    result = tai.swap_by_newest(jesse)

    assert result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 4
    assert jesse.inventory == [item_f, item_g, item_c]
    assert tai.inventory == [item_a, item_b, item_d, item_e]