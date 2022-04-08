import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_clothing_has_age_default_None(): 
    clothing = Clothing()
    assert clothing.age == None

def test_decor_has_age_default_None(): 
    decor = Decor()
    assert decor.age == None

def test_electronics_has_age_default_None(): 
    electronics = Electronics()
    assert electronics.age == None

def test_newest_by_category():
    item_a = Clothing(age=2)
    item_b = Decor(age=1)
    item_c = Clothing(age=5)
    ryan = Vendor(inventory=[item_a, item_b, item_c])

    newest_item = ryan.get_newest_by_category("Clothing")

    assert newest_item.age == 2
    assert newest_item.category == "Clothing"

def test_newest_by_category_no_matches_is_none():
    item_a = Electronics(age=3)
    item_b = Decor(age=7)
    item_c = Decor(age=5)
    tara = Vendor(inventory=[item_a, item_b, item_c])

    newest_item = tara.get_newest_by_category("Clothing")

    assert newest_item == None

def test_newest_by_category_with_duplicates():
    item_a = Clothing(age=2)
    item_b = Clothing(age=2)
    item_c = Clothing(age=4)
    robin = Vendor(inventory=[item_a, item_b, item_c])

    newest_item = robin.get_newest_by_category("Clothing")

    assert newest_item.age == 2
    assert newest_item.category == "Clothing"

def test_swap_newest_by_category():
    item_a = Decor(age=9)
    item_b = Clothing(age=2)
    item_c = Decor(age=3)
    thomas = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Electronics(age=3)
    item_e = Decor(age=3)
    item_f = Electronics(age=1)
    stevie = Vendor(inventory=[item_d, item_e, item_f])

    result = thomas.swap_newest_by_category(
        other=stevie, 
        my_priority="Electronics", 
        their_priority="Decor"
    )

    assert result is True
    assert len(thomas.inventory) == 3
    assert len(stevie.inventory) == 3
    assert item_c in stevie.inventory
    assert item_f in thomas.inventory

def test_swap_newest_by_category_no_inventory_is_false():
    item_a = Clothing(age=9)
    item_b = Clothing(age=2)
    item_c = Clothing(age=3)
    charlotte = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Electronics(age=3)
    item_e = Decor(age=3)
    item_f = Electronics(age=1)
    parker = Vendor(inventory=[item_d, item_e, item_f])

    result = charlotte.swap_newest_by_category(
        other=parker,
        my_priority="Decor",
        their_priority="Electronics"
    )

    assert result is False
    assert len(charlotte.inventory) == 3
    assert len(parker.inventory) == 3
    for item in charlotte.inventory:
        assert item.category != "Electronics"

def test_swap_newest_by_category_no_other_inventory_is_false():
    item_a = Decor(age=3)
    item_b = Electronics(age=1)
    item_c = Clothing(age=5)
    sage = Vendor(inventory=[item_a, item_b, item_c])

    audrey = Vendor(inventory=[])

    result = sage.swap_newest_by_category(
        other=audrey, 
        my_priority="Decor", 
        their_priority="Clothing"
    )

    assert not result
    assert len(sage.inventory) == 3
    assert len(audrey.inventory) == 0 
    assert item_a in sage.inventory
    assert item_b in sage.inventory
    assert item_c in sage.inventory