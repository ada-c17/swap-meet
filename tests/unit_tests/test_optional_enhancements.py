import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_newest():
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=1.0)
    nina = Vendor(
        inventory=[item_a, item_b, item_c])

    newest_item = nina.get_newest(2.0)

    assert newest_item.category == "Decor"
    assert newest_item.age == pytest.approx(1.0)

def test_get_newest_no_matches_is_none():
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=4.0)
    nina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = nina.get_newest(1.0)

    assert newest_item is None

def test_get_newest_with_duplicates():
    item_a = Decor(age=1.0)
    item_b = Electronics(age=1.0)
    item_c = Decor(age=4.0)
    nina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = nina.get_newest(1.0)

    assert newest_item.category == "Decor"
    assert newest_item.age == pytest.approx(1.0)

def test_get_newest_with_empty_inventory_is_none():
    nina = Vendor(
        inventory=[]
    )

    newest_item = nina.get_newest(1.0)

    assert newest_item is None

def test_swap_by_newest():
    # self
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=1.0)
    nina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # other
    item_d = Clothing(age=3.0)
    item_e = Decor(age=4.5)
    item_f = Clothing(age=1.0)
    jeff = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = nina.swap_by_newest(
        other=jeff,
        my_priority=1.0,
        their_priority=1.0
    )

    assert result
    assert len(nina.inventory) == 3
    assert len(jeff.inventory) == 3
    assert item_a in nina.inventory
    assert item_b in nina.inventory
    assert item_c not in nina.inventory
    assert item_f in nina.inventory
    assert item_d in jeff.inventory
    assert item_e in jeff.inventory
    assert item_f not in jeff.inventory
    assert item_c in jeff.inventory

def test_swap_by_newest_by_category_reordered():
    # self
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=1.0)
    nina = Vendor(
        inventory=[item_c, item_a, item_b]
    )

    # other
    item_d = Clothing(age=3.0)
    item_e = Decor(age=4.5)
    item_f = Clothing(age=1.0)
    jeff = Vendor(
        inventory=[item_f, item_d, item_e]
    )

    result = nina.swap_by_newest(
        other=jeff,
        my_priority=1.0,
        their_priority=1.0
    )

    assert result
    assert len(nina.inventory) == 3
    assert len(jeff.inventory) == 3
    assert item_a in nina.inventory
    assert item_b in nina.inventory
    assert item_c not in nina.inventory
    assert item_f in nina.inventory
    assert item_d in jeff.inventory
    assert item_e in jeff.inventory
    assert item_f not in jeff.inventory
    assert item_c in jeff.inventory

def test_swap_by_newest_no_inventory_returns_false():
    # self
    nina = Vendor(
        inventory=[]
    )

    # other
    item_d = Clothing(age=3.0)
    item_e = Decor(age=4.5)
    item_f = Clothing(age=1.0)
    jeff = Vendor(
        inventory=[item_f, item_d, item_e]
    )

    result = nina.swap_by_newest(
        other=jeff,
        my_priority=1.0,
        their_priority=1.0
    )

    assert result == False
    assert len(nina.inventory) == 0
    assert len(jeff.inventory) == 3
    assert item_d in jeff.inventory
    assert item_e in jeff.inventory
    assert item_f in jeff.inventory

def test_swap_by_newest_no_other_inventory_returns_false():
    # self
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=1.0)
    nina = Vendor(
        inventory=[item_c, item_a, item_b]
    )

    # other
    jeff = Vendor(
        inventory=[]
    )

    result = nina.swap_by_newest(
        other=jeff,
        my_priority=1.0,
        their_priority=1.0
    )

    assert result == False
    assert len(nina.inventory) == 3
    assert len(jeff.inventory) == 0
    assert item_a in nina.inventory
    assert item_b in nina.inventory
    assert item_c in nina.inventory

def test_swap_by_newest_no_match_returns_false():
    # self
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=1.0)
    nina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # other
    item_d = Clothing(age=3.0)
    item_e = Decor(age=4.5)
    item_f = Clothing(age=2.0)
    jeff = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = nina.swap_by_newest(
        other=jeff,
        my_priority=1.0,
        their_priority=1.0
    )

    assert result == False
    assert len(nina.inventory) == 3
    assert len(jeff.inventory) == 3
    assert item_a in nina.inventory
    assert item_b in nina.inventory
    assert item_c in nina.inventory
    assert item_d in jeff.inventory
    assert item_e in jeff.inventory
    assert item_f in jeff.inventory

def test_swap_by_newest_no_other_match_returns_false():
    # self
    item_a = Decor(age=2.0)
    item_b = Electronics(age=5.0)
    item_c = Decor(age=4.0)
    nina = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # other
    item_d = Clothing(age=3.0)
    item_e = Decor(age=4.5)
    item_f = Clothing(age=1.0)
    jeff = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = nina.swap_by_newest(
        other=jeff,
        my_priority=1.0,
        their_priority=1.0
    )

    assert result == False
    assert len(nina.inventory) == 3
    assert len(jeff.inventory) == 3
    assert item_a in nina.inventory
    assert item_b in nina.inventory
    assert item_c in nina.inventory
    assert item_d in jeff.inventory
    assert item_e in jeff.inventory
    assert item_f in jeff.inventory
