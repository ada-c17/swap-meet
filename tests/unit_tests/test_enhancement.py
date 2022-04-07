import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

item_a = Clothing(0, 0)
item_b = Clothing(0, 1)
item_c = Electronics(0, 2)

item_d = Decor(3, 1)
item_e = Decor(4, 2)
item_f = Clothing(0, 3)

def test_swap_by_newest_return_true():
    # Arrange
    inventory_1 = [item_a, item_b, item_c]
    vendor_1 = Vendor(inventory=inventory_1)

    inventory_2 = [item_d, item_e, item_f]
    vendor_2 = Vendor(inventory=inventory_2)

    # Act    
    result = vendor_1.swap_by_newest(vendor_2)

    # Assert
    assert result == True
    assert len(vendor_1.inventory) == 3
    assert len(vendor_2.inventory) == 3
    assert item_d in vendor_1.inventory and item_d not in vendor_2.inventory
    assert item_a in vendor_2.inventory and item_a not in vendor_1.inventory

def test_swap_by_newest_with_empty_inventory():
    # Arrange
    vendor_1 = Vendor()

    inventory = [item_d, item_e, item_f]
    vendor_2 = Vendor(inventory=inventory)

    # Act
    result = vendor_1.swap_by_newest(vendor_2)

    # Assert
    assert result == False
    assert len(vendor_1.inventory) == 0
    assert len(vendor_2.inventory) == 3
    assert vendor_1.inventory == []
    assert vendor_2.inventory == [item_d, item_e, item_f]

def test_swap_by_newest_with_tie():
    # Arrange
    inventory_1 = [item_f, item_b, item_d]
    vendor_1 = Vendor(inventory=inventory_1)

    inventory_2 = [item_c, item_e]
    vendor_2 = Vendor(inventory=inventory_2)

    # Arrange
    result = vendor_1.swap_by_newest(vendor_2)

    # Assert
    assert result == True
    assert len(vendor_1.inventory) == 3
    assert len(vendor_2.inventory) == 2
    assert item_b in vendor_2.inventory and item_b not in vendor_1.inventory
    assert item_c in vendor_1.inventory and item_c not in vendor_2.inventory

def test_get_newest_return_newest_item():
    # Arrange
    inventory = [item_a, item_b, item_c]
    vendor = Vendor(inventory)

    # Arrange
    result = vendor.get_newest()

    # Assert
    assert result == item_a
    assert len(vendor.inventory) == 3

def test_get_newest_return_newest_item_reordered():
    # Arrange
    inventory = [item_b, item_c, item_a]
    vendor = Vendor(inventory)

    # Arrange
    result = vendor.get_newest()

    # Assert
    assert result == item_a
    assert len(vendor.inventory) == 3

def test_get_newest_no_inventory_return_false():
    # Arrange
    vendor = Vendor()

    # Arrange
    result = vendor.get_newest()

    # Assert
    assert result == False
    assert not vendor.inventory

def test_get_newest_tie_return_first_item():
        # Arrange
    inventory = [item_b, item_c, item_d]
    vendor = Vendor(inventory)

    # Arrange
    result = vendor.get_newest()

    # Assert
    assert result == item_b
    assert len(vendor.inventory) == 3