import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

# @pytest.mark.skip
def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_category("Clothing")

    # Assert
    assert best_item.category == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    assert result is True
    # - That tai and jesse's inventories are the correct length
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    # test items are in tai's inventories
    assert tai.inventory[0] == item_a
    assert tai.inventory[0].condition == 2
    assert tai.inventory[0].category == "Decor"
    assert tai.inventory[1] == item_b
    assert tai.inventory[1].condition == 4
    assert tai.inventory[1].category == "Electronics"
    assert tai.inventory[2] == item_f
    assert tai.inventory[2].condition == 4
    assert tai.inventory[2].category == "Clothing"
    # test swapped item is not in the tai's inventory
    for item in tai.inventory:
        assert item != item_c
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[0].category == "Clothing"
    assert jesse.inventory[0].condition == 2
    assert jesse.inventory[1] == item_e
    assert jesse.inventory[1].category == "Decor"
    assert jesse.inventory[1].condition == 4
    assert jesse.inventory[2] == item_c
    assert jesse.inventory[2].category == "Decor"
    assert jesse.inventory[2].condition == 4
    # test swapped item is not in the jesse's inventory
    for item in jesse.inventory:
        assert item != item_f

# @pytest.mark.skip
def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    assert result is True
    # - That tai and jesse's inventories are the correct length
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there
    # test items are in tai's inventories
    assert tai.inventory[0] == item_b
    assert tai.inventory[0].condition == 4
    assert tai.inventory[0].category == "Electronics"
    assert tai.inventory[1] == item_a
    assert tai.inventory[1].condition == 2
    assert tai.inventory[1].category == "Decor"
    assert tai.inventory[2] == item_f
    assert tai.inventory[2].condition == 4
    assert tai.inventory[2].category == "Clothing"
    # test swapped item is not in the tai's inventory
    for item in tai.inventory:
        assert item != item_c 
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_e
    assert jesse.inventory[0].category == "Decor"
    assert jesse.inventory[0].condition == 4
    assert jesse.inventory[1] == item_d
    assert jesse.inventory[1].category == "Clothing"
    assert jesse.inventory[1].condition == 2
    assert jesse.inventory[2] == item_c
    assert jesse.inventory[2].category == "Decor"
    assert jesse.inventory[2].condition == 4
    # test swapped item is not in the jesse's inventory
    for item in jesse.inventory:
        assert item != item_f

# @pytest.mark.skip
def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    assert result is False
    # - That tai and jesse's inventories are the correct length
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories
    # test items are in tai's inventories
    assert tai.inventory[0] == item_a
    assert tai.inventory[0].condition == 2
    assert tai.inventory[0].category == "Decor"
    assert tai.inventory[1] == item_b
    assert tai.inventory[1].condition == 4
    assert tai.inventory[1].category == "Electronics"
    assert tai.inventory[2] == item_c
    assert tai.inventory[2].condition == 4
    assert tai.inventory[2].category == "Decor"
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[0].category == "Clothing"
    assert jesse.inventory[0].condition == 2
    assert jesse.inventory[1] == item_e
    assert jesse.inventory[1].category == "Decor"
    assert jesse.inventory[1].condition == 4
    assert jesse.inventory[2] == item_f
    assert jesse.inventory[2].category == "Clothing"
    assert jesse.inventory[2].condition == 4

# @pytest.mark.skip
def test_swap_best_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    assert result is False
    # - That tai and jesse's inventories are the correct length
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories
    # test items are in tai's inventories
    assert tai.inventory[0] == item_c
    assert tai.inventory[0].condition == 4
    assert tai.inventory[0].category == "Decor"
    assert tai.inventory[1] == item_b
    assert tai.inventory[1].condition == 4
    assert tai.inventory[1].category == "Electronics"
    assert tai.inventory[2] == item_a
    assert tai.inventory[2].condition == 2
    assert tai.inventory[2].category == "Decor"
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_f
    assert jesse.inventory[0].category == "Clothing"
    assert jesse.inventory[0].condition == 4
    assert jesse.inventory[1] == item_e
    assert jesse.inventory[1].category == "Decor"
    assert jesse.inventory[1].condition == 4
    assert jesse.inventory[2] == item_d
    assert jesse.inventory[2].category == "Clothing"
    assert jesse.inventory[2].condition == 2