import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_age_condition_same_across_classes():
    items = [
        Clothing(age=5),
        Decor(age=5),
        Electronics(age=5)
    ]
    five_age_description = items[0].age_description()
    assert isinstance(five_age_description, str)
    for item in items:
        assert item.age_description() == five_age_description

    items[0].age = 1
    one_age_description = items[0].age_description()
    assert isinstance(one_age_description, str)

    for item in items:
        item.age = 1
        assert item.age_description() == one_age_description

    assert one_age_description != five_age_description

# @pytest.mark.skip
def test_get_newest_item():
    item_a = Clothing(age=25.0)
    item_b = Decor(age=13.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=10.0)
    item_e = Clothing(age=8.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest_item()

    assert newest_item == item_c


# @pytest.mark.skip
def test_get_newest_item_unknown_age_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = tai.get_newest_item()

    assert newest_item is None


# @pytest.mark.skip
def test_get_newest_item_with_duplicates():
    # Arrange
    item_a = Clothing(age=1.0)
    item_b = Clothing(age=1.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    newest_item = tai.get_newest_item()

    # Assert
    assert newest_item is item_a


# @pytest.mark.skip
def test_get_newest_item_with_duplicates_shuffle_order():
    # Arrange
    item_a = Clothing(age=10.0)
    item_b = Clothing(age=1.0)
    item_c = Clothing(age=1.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    newest_item = tai.get_newest_item()

    # Assert
    assert newest_item is item_b


# @pytest.mark.skip
def test_get_newest_item_some_ages_unknown_ignores_unknowns():
    # Arrange
    item_a = Clothing(age=1.0)
    item_b = Clothing()
    item_c = Clothing(age=4.0)
    item_d = Decor()
    item_e = Electronics(age=0.5)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    # Act
    newest_item = tai.get_newest_item()

    # Assert
    assert newest_item is item_e


# @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=4.0, age=5)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=6)
    item_e = Decor(condition=4.0, age=2)
    item_f = Clothing(condition=4.0, age=15)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    # Assert
    assert result
    assert len(tai.inventory) and len(jesse.inventory) == 3
    assert item_e and item_b and item_c in tai.inventory
    assert item_a and item_d and item_f in jesse.inventory
    assert item_a not in tai.inventory
    assert item_e not in jesse.inventory


# @pytest.mark.skip
def test_swap_by_newest_self_empty_inventory_returns_false():
    # Arrange
    tai = Vendor(
        inventory=[]
    )

    item_d = Clothing(condition=2.0, age=6)
    item_e = Decor(condition=4.0, age=2)
    item_f = Clothing(condition=4.0, age=15)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    # Assert
    assert not result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 0
    assert item_e and item_d and item_f in jesse.inventory


# @pytest.mark.skip
def test_swap_by_newest_other_empty_inventory_returns_false():
        # Arrange
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=4.0, age=5)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    # Assert
    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a and item_b and item_c in tai.inventory


# @pytest.mark.skip
def test_swap_by_newest_all_items_age_unknown_returns_false():
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
    result = tai.swap_by_newest(jesse)

    # Assert

    assert not result
    assert len(tai.inventory) and len(jesse.inventory) == 3
    assert item_a and item_b and item_c in tai.inventory
    assert item_d and item_e and item_f in jesse.inventory


# @pytest.mark.skip
def test_swap_by_newest_self_items_age_unknown_returns_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=1)
    item_e = Decor(condition=4.0, age=4)
    item_f = Clothing(condition=4.0, age=100)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(jesse)

    # Assert

    assert not result
    assert len(tai.inventory) and len(jesse.inventory) == 3
    assert item_a and item_b and item_c in tai.inventory
    assert item_d and item_e and item_f in jesse.inventory


# @pytest.mark.skip
def test_swap_by_newest_other_items_age_unknown_returns_false():
    # Arrange
    item_a = Decor(condition=2.0, age=4)
    item_b = Electronics(condition=4.0, age=7)
    item_c = Decor(condition=4.0, age=6)
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
    result = tai.swap_by_newest(jesse)

    # Assert

    assert not result
    assert len(tai.inventory) and len(jesse.inventory) == 3
    assert item_a and item_b and item_c in tai.inventory
    assert item_d and item_e and item_f in jesse.inventory
