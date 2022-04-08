import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

# ---------- TEST ONE ---------- #
# ---------- PASSED ---------- # 
# @pytest.mark.skip
def test_items_have_blank_default_category():
    item = Item()
    assert item.category == ""

# ---------- TEST TWO ---------- #
# ---------- PASSED ---------- # 
# @pytest.mark.skip
def test_get_items_by_category():
    item_a = Item(category="clothing")
    item_b = Item(category="electronics")
    item_c = Item(category="clothing")
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("clothing")

    assert len(items) == 2
    assert item_a in items
    assert item_c in items
    assert item_b not in items

# ---------- TEST THREE ---------- #
# ---------- PASSED ---------- # 
# @pytest.mark.skip
def test_get_no_matching_items_by_category():
    item_a = Item(category="clothing")
    item_b = Item(category="clothing")
    item_c = Item(category="clothing")
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_by_category("electronics")

    assert len(items) == 0
