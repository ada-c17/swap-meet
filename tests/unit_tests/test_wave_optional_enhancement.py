import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_swap_by_newest_returns_true():
    item_a = Item(1)
    item_b = Item(2)
    item_c = Item(2)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(2)
    item_e = Item(3)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert result
    assert len(fatimah.inventory) == 3
    assert item_a not in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_c in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory

def test_swap_by_newest_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(2)
    item_e = Item(3)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert not result
    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2

def test_swap_newest_item_from_their_empty_returns_false():
    item_a = Item(1)
    item_b = Item(2)
    item_c = Item(2)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )

    result = fatimah.swap_by_newest(jolie)

    assert not result
    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 0
    