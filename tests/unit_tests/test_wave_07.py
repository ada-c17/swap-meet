from unittest import result
import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_get_newest_item():
    item_a = Item(age=10)
    item_b = Item(age=9)
    item_c = Item(age=8)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = fatimah.get_newest_item()

    # assert result
    assert result == item_c
    assert result != item_a



def test_swap_by_newest():
    item_a = Item(age=10)
    item_b = Item(age=9)
    item_c = Item(age=8)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=12)
    item_e = Item(age=2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_c not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_b in fatimah.inventory
    assert item_e in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_e not in jolie.inventory
    assert item_d in jolie.inventory
    assert item_c in jolie.inventory
    assert result