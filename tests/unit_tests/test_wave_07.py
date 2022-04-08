import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# Test 34
#@pytest.mark.skip
def test_age_statement_by_default():
    item = Item()
    item_age = item.age_statement()

    assert item.age == 0
    assert item_age == "This item was made 0 months ago."


# Test 35
#@pytest.mark.skip
def test_age_statement_with_different_value():
    item = Item(age = 7)
    item_age = item.age_statement()

    assert item_age == "This item was made 7 months ago."


# Test 36
#@pytest.mark.skip
def test_get_newest_item():
    item_a = Clothing(age=1)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    nishat = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = nishat.get_newest_item()

    assert newest_item
    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(1)


# Test 37
#@pytest.mark.skip
def test_newest_item_is_empty():
    # item_a = Clothing(age=2)
    # item_b = Decor(age=2)
    # item_c = Clothing(age=4)
    # item_d = Decor(age=5)
    # item_e = Clothing(age=3)
    nishat = Vendor(
        inventory=[]
    )

    newest_item = nishat.get_newest_item()

    assert newest_item is None


# Test 38
#@pytest.mark.skip
def test_get_newest_item_with_duplicates_returns_first_item():
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    nishat = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = nishat.get_newest_item()

    
    assert newest_item.age == 2
    assert newest_item == item_a
    

# Test 39
#@pytest.mark.skip
def test_swap_newest_item():
    # Arrange
    item_a = Decor(age=12)
    item_b = Electronics(age=8)
    item_c = Decor(age=9)
    nishat = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=4)
    item_e = Decor(age=7)
    item_f = Clothing(age=14)
    fatima = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = nishat.swap_by_newest(
        other = fatima,
        my_item = fatima.get_newest_item(),
        their_item = nishat.get_newest_item()
    )

    assert result
    assert len(nishat.inventory) == 3
    assert len(fatima.inventory) == 3
    assert item_a in nishat.inventory
    assert item_b not in nishat.inventory
    assert item_b in fatima.inventory
    assert item_c in nishat.inventory
    assert item_d not in fatima.inventory
    assert item_d in nishat.inventory
    assert item_e in fatima.inventory
    assert item_f in fatima.inventory


# Test 40
#@pytest.mark.skip
def test_swap_newest_item_reordered():
    # Arrange
    item_a = Decor(age=12)
    item_b = Electronics(age=8)
    item_c = Decor(age=9)
    nishat = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=4)
    item_e = Decor(age=7)
    item_f = Clothing(age=14)
    fatima = Vendor(
        inventory=[item_e, item_d, item_f]
    )

    # Act
    result = nishat.swap_by_newest(
        other = fatima,
        my_item = fatima.get_newest_item(),
        their_item = nishat.get_newest_item()
    )

    assert result
    assert len(nishat.inventory) == 3
    assert len(fatima.inventory) == 3
    assert item_a in nishat.inventory
    assert item_b not in nishat.inventory
    assert item_b in fatima.inventory
    assert item_c in nishat.inventory
    assert item_d not in fatima.inventory
    assert item_d in nishat.inventory
    assert item_e in fatima.inventory
    assert item_f in fatima.inventory
    

# Test 41
#@pytest.mark.skip
def test_swap_newest_item_self_inventory_empty():
    # Arrange
    nishat = Vendor(
        inventory=[]
    )

    item_d = Clothing(age=4)
    item_e = Decor(age=7)
    item_f = Clothing(age=14)
    fatima = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = nishat.swap_by_newest(
        other = fatima,
        my_item = fatima.get_newest_item(),
        their_item = nishat.get_newest_item()
    )

    assert not result
    assert len(nishat.inventory) == 0
    assert len(fatima.inventory) == 3
    assert item_d in fatima.inventory
    assert item_e in fatima.inventory
    assert item_f in fatima.inventory
    

# Test 42
#@pytest.mark.skip
def test_swap_newest_item_other_inventory_empty():
    # Arrange
    item_a = Decor(age=12)
    item_b = Electronics(age=8)
    item_c = Decor(age=9)
    nishat = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    fatima = Vendor(
        inventory=[]
    )

    # Act
    result = nishat.swap_by_newest(
        other = fatima,
        my_item = fatima.get_newest_item(),
        their_item = nishat.get_newest_item()
    )

    assert not result
    assert len(nishat.inventory) == 3
    assert len(fatima.inventory) == 0
    assert item_a in nishat.inventory
    assert item_b in nishat.inventory
    assert item_c in nishat.inventory