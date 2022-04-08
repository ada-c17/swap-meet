import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item 


# ***************************************************************
# Optional Enhancement Tests
# ****************************************************************
def test_get_by_newest():
    item_a = Item(category="clothing", age=4.0)
    item_b = Item(category="decor", age=2.0)
    item_c = Item(category="clothing", age=1.0)
    item_d = Item(category="decor", age=5.0)
    item_e = Item(category="clothing", age=3.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = luke.get_by_newest("clothing")

    assert newest_item.category == "clothing"
    assert newest_item.age == pytest.approx(1.0)


def test_get_by_newest_no_matches_is_none():
    item_a = Item(category="clothing", age=4.0)
    item_b = Item(category="decor", age=2.0)
    item_c = Item(category="clothing", age=1.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = luke.get_by_newest("electronics")

    assert best_item is None


def test_get_by_newest_with_duplicates():
    # Arrange
    item_a = Item(category="clothing", age=4.0)
    item_b = Item(category="decor", age=2.0)
    item_c = Item(category="clothing", age=4.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = luke.get_by_newest("clothing")

    # Assert
    assert best_item.category == "clothing"
    assert best_item.age == pytest.approx(4.0)


def test_swap_by_newest():
    # Arrange
    # me
    item_a = Item(category="electronics", age=2.0)
    item_b = Item(category="electronics", age=4.0)
    item_c = Item(category="decor", age=4.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Item(category="clothing", age=2.0)
    item_e = Item(category="decor", age=4.0)
    item_f = Item(category="clothing", age=1.0)
    leia = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = luke.swap_by_newest(
        other=leia,
        my_priority_newest ="clothing",
        their_priority_newest="electronics"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    assert result is True 
    # - That luke and leia's inventories are the correct length
    assert len(luke.inventory) == 3
    assert len(leia.inventory) == 3
    # - That all the correct items are in luke and leia's inventories, including the items which were swapped from one vendor to the other
    assert item_a not in luke.inventory
    assert item_a in leia.inventory 
    assert item_b in luke.inventory
    assert item_c in luke.inventory
    assert item_d in leia.inventory
    assert item_e in leia.inventory
    assert item_f not in leia.inventory
    assert item_f in luke.inventory 


def test_swap_best_by_category_reordered():
    # Arrange
    # me
    item_a = Item(category="electronics", age=2.0)
    item_b = Item(category="electronics", age=4.0)
    item_c = Item(category="decor", age=4.0)
    luke = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    # them
    item_d = Item(category="clothing", age=2.0)
    item_e = Item(category="decor", age=4.0)
    item_f = Item(category="clothing", age=1.0)
    leia = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = luke.swap_by_newest(
        other=leia,
        my_priority_newest ="clothing",
        their_priority_newest="electronics"
    )

    # - That the results is truthy
    assert result is True 
    # - That luke and leia's inventories are the correct length
    assert len(luke.inventory) == 3
    assert len(leia.inventory) == 3
    # - That all the correct items are in luke and leia's inventories, including the items which were swapped from one vendor to the other
    assert item_a not in luke.inventory
    assert item_a in leia.inventory 
    assert item_b in luke.inventory
    assert item_c in luke.inventory
    assert item_d in leia.inventory
    assert item_e in leia.inventory
    assert item_f not in leia.inventory
    assert item_f in luke.inventory 


def test_swap_by_newest_no_inventory_is_false():
    luke = Vendor(
        inventory=[]
    )

    item_a = Item(category="electronics", age=2.0)
    item_b = Item(category="electronics", age=4.0)
    item_c = Item(category="decor", age=4.0)
    leia = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = luke.swap_by_newest(
        other=leia,
        my_priority_newest="clothing",
        their_priority_newest="decor"
    )

    assert not result
    assert len(luke.inventory) == 0
    assert len(leia.inventory) == 3
    assert item_a in leia.inventory
    assert item_b in leia.inventory
    assert item_c in leia.inventory


def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Item(category="electronics", age=2.0)
    item_b = Item(category="electronics", age=4.0)
    item_c = Item(category="decor", age=4.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    leia = Vendor(
        inventory=[]
    )

    result = luke.swap_by_newest(
        other=leia,
        my_priority_newest="decor",
        their_priority_newest="clothing"
    )

    assert not result
    assert len(luke.inventory) == 3
    assert len(leia.inventory) == 0
    assert item_a in luke.inventory
    assert item_b in luke.inventory
    assert item_c in luke.inventory


def test_swap_by_newest_no_match_is_false():
    # Arrange
    item_a = Item(category="decor", age=2.0)
    item_b = Item(category="electronics", age=4.0)
    item_c = Item(category="decor", age=4.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="clothing", age=2.0)
    item_e = Item(category="decor", age=4.0)
    item_f = Item(category="clothing", age=4.0)
    leia = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = luke.swap_by_newest(
        other=leia,
        my_priority_newest="clothing",
        their_priority_newest="clothing"
    )

    # - That result is falsy
    assert result is False 
    # - That luke and leia's inventories are the correct length
    assert len(luke.inventory) == 3
    assert len(leia.inventory) == 3
    # - That all the correct items are in luke and leia's inventories
    assert item_a in luke.inventory
    assert item_b in luke.inventory
    assert item_c in luke.inventory
    assert item_d in leia.inventory
    assert item_e in leia.inventory
    assert item_f in leia.inventory


def test_swap_by_newest_no_other_match_is_false():
    # Arrange
    item_a = Item(category="decor", age=2.0)
    item_b = Item(category="electronics", age=4.0)
    item_c = Item(category="decor", age=4.0)
    luke = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="clothing", age=2.0)
    item_e = Item(category="decor", age=4.0)
    item_f = Item(category="clothing", age=4.0)
    leia = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = luke.swap_by_newest(
        other=leia,
        my_priority_newest="electronics",
        their_priority_newest="decor"
    )

    # - That result is falsy
    assert result is False 
    # - That luke and leia's inventories are the correct length
    assert len(luke.inventory) == 3
    assert len(leia.inventory) == 3
    # - That all the correct items are in luke and leia's inventories
    assert item_a in luke.inventory
    assert item_b in luke.inventory
    assert item_c in luke.inventory
    assert item_d in leia.inventory
    assert item_e in leia.inventory
    assert item_f in leia.inventory