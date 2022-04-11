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
    assert len(jenn.inventory) == 3 and len(alex.inventory) == 3
    assert item_c not in jenn.inventory
    assert [item_a, item_b, item_e] == jenn.inventory
    assert item_e not in alex.inventory
    assert [item_d, item_f, item_c] == alex.inventory

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
    assert len(jenn.inventory) == 0 and len(alex.inventory) == 3
    assert [item_a, item_b, item_c] == alex.inventory

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
    assert len(jenn.inventory) == 3 and len(alex.inventory) == 0
    assert [item_a, item_b, item_c] == jenn.inventory

def test_swap_by_newest_None_age_is_false():
    item_a = Clothing()
    jenn = Vendor(inventory=[item_a])

    item_b = Clothing(age=2)
    item_c = Decor(age=4)
    item_d = Electronics(age=1)
    alex = Vendor(
        inventory=[item_b, item_c, item_d]
    )

    result = jenn.swap_by_newest(alex)

    assert not result
    assert len(jenn.inventory) == 1 and len(alex.inventory) == 3
    assert [item_a] == jenn.inventory
    assert [item_b, item_c, item_d] == alex.inventory

def test_swap_by_newest_inventory_with_Nones_still_works():
    item_a = Clothing(age=2)
    item_b = Decor()
    item_c = Electronics(age=1)
    jenn = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor()
    item_e = Clothing(age=3)
    item_f = Decor(age=25)
    alex = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = jenn.swap_by_newest(alex)

    assert result
    assert len(jenn.inventory) == 3 and len(alex.inventory) == 3
    assert item_c not in jenn.inventory
    assert [item_a, item_b, item_e] == jenn.inventory
    assert item_e not in alex.inventory
    assert [item_d, item_f, item_c] == alex.inventory