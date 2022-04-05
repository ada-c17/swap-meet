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