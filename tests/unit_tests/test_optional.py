import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Electronics(age=1)
    jenn = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(age=12)
    item_e = Clothing(age=3)
    item_f = Decor(age=25)
    alex = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = jenn.swap_by_newest(alex)

    assert result
    assert len(jenn.inventory) == 3
    assert len(alex.inventory) == 3
    assert item_c not in jenn.inventory
    assert item_a in jenn.inventory
    assert item_b in jenn.inventory
    assert item_e in jenn.inventory
    assert item_e not in alex.inventory
    assert item_d in alex.inventory
    assert item_f in alex.inventory
    assert item_c in alex.inventory

def test_swap_by_newest_no_inventory_is_false():
    jenn = Vendor()

    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Electronics(age=1)
    alex = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = jenn.swap_by_newest(alex)

    assert not result
    assert len(jenn.inventory) == 0
    assert len(alex.inventory) == 3
    assert item_a in alex.inventory
    assert item_b in alex.inventory
    assert item_c in alex.inventory

def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Electronics(age=1)
    jenn = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    alex = Vendor()

    result = jenn.swap_by_newest(alex)

    assert not result
    assert len(jenn.inventory) == 3
    assert len(alex.inventory) == 0
    assert item_a in jenn.inventory
    assert item_b in jenn.inventory
    assert item_c in jenn.inventory