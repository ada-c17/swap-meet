import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_item_has_correct_age():
    item = Item(age=1)
    assert item.age == 1

def test_item_with_no_age():
    item = Item()
    assert item.age is None

def test_clothing_has_correct_age():
    item = Clothing(age=2)
    assert item.age == 2

def test_clothing_with_no_age():
    item = Clothing()
    assert item.age is None

def test_decor_has_correct_age():
    item = Decor(age=4.2)
    assert item.age == 4.2

def test_decor_has_no_age():
    item = Decor()
    assert item.age is None

def test_electronics_has_correct_age():
    item = Electronics(age=4)
    assert item.age == 4

def test_electronics_has_no_age():
    item = Electronics()
    assert item.age is None


def test_get_newest():
    item_a = Decor(age=1)
    item_b = Electronics()
    item_c = Clothing(age=0.5)

    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item =  tai.get_newest_item()
    assert newest_item == item_c


def test_get_newest_with_ties():
    item_a = Decor(age=0.5)
    item_b = Electronics()
    item_c = Clothing(age=0.5)

    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item =  tai.get_newest_item()
    assert newest_item == item_a


def test_get_newest_no_age_is_False():
    item_a = Decor()
    item_b = Electronics()
    item_c = Clothing()

    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item =  tai.get_newest_item()
    assert newest_item is None


def test_swap_newest():
    # me
    item_a = Decor(age=0.5)
    item_b = Electronics()
    item_c = Clothing(age=0.5)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Electronics(age=2.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other=jesse)

    assert result is True
    assert len(tai.inventory) == 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_d not in jesse.inventory


def test_swap_newest_missing_my_ages_is_False():
    # me
    item_a = Decor()
    item_b = Electronics()
    item_c = Clothing()
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Electronics(age=2.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other=jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


def test_swap_newest_missing_their_ages_is_False():
    # me
    item_a = Decor(age=1)
    item_b = Electronics()
    item_c = Clothing()
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing()
    item_e = Decor()
    item_f = Electronics()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other=jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


def test_swap_newest_missing_ages_is_False():
    # me
    item_a = Decor()
    item_b = Electronics()
    item_c = Clothing()
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing()
    item_e = Decor()
    item_f = Electronics()
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(other=jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory