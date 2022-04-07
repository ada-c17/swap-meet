import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.electronics import Electronics
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor

def test_swap_by_newest_returns_false_no_age_for_both():
    item_a = Electronics()
    item_b = Clothing()
    jojo = Vendor(inventory=[item_a])
    kiki = Vendor(inventory=[item_b])

    result = jojo.swap_by_newest(kiki)

    assert result is False
    assert item_a in jojo.inventory
    assert len(jojo.inventory) == 1
    assert item_b in kiki.inventory
    assert len(kiki.inventory) == 1

def test_swap_newest_returns_false_one_vendor_no_age():
    item_a = Electronics(age=1)
    item_b = Clothing(age=9)
    item_c = Decor()
    item_d = Clothing()
    jojo = Vendor(inventory=[item_a, item_b])
    kiki = Vendor(inventory=[item_c, item_d])

    result = jojo.swap_by_newest(kiki)

    assert result is False
    assert item_a in jojo.inventory
    assert item_b in jojo.inventory
    assert len(jojo.inventory) == 2
    assert item_c in kiki.inventory
    assert item_d in kiki.inventory
    assert len(kiki.inventory) == 2

def test_swap_by_newest_returns_true():
    item_a = Decor(age=10)
    item_b = Decor(age=12)
    item_c = Clothing(age=3)
    jojo = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(age=5)
    item_e = Electronics(age=2)
    item_f = Decor(age=7)
    kiki = Vendor(inventory=[item_d, item_e, item_f])

    result = jojo.swap_by_newest(kiki)

    assert result is True
    assert len(jojo.inventory) == 3
    assert len(kiki.inventory) == 3
    assert item_a in jojo.inventory
    assert item_b in jojo.inventory
    assert item_c in kiki.inventory
    assert item_d in kiki.inventory
    assert item_e in jojo.inventory
    assert item_f in kiki.inventory

def test_swap_by_newest_swaps_first_items_if_tie():
    item_a = Decor(age=3)
    item_b = Decor(age=3)
    item_c = Clothing(age=3)
    jojo = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(age=2)
    item_e = Electronics(age=2)
    item_f = Decor(age=2)
    kiki = Vendor(inventory=[item_d, item_e, item_f]) 

    result = jojo.swap_by_newest(kiki)
    
    assert result is True
    assert len(jojo.inventory) == 3
    assert len(kiki.inventory) == 3
    assert item_a in kiki.inventory
    assert item_b in jojo.inventory
    assert item_c in jojo.inventory
    assert item_d in jojo.inventory
    assert item_e in kiki.inventory
    assert item_f in kiki.inventory