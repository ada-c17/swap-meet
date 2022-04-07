import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_missing_condition_descriptions():
    items = [
        Clothing(condition=4.5),
        Decor(condition=4),
        Electronics(condition=2.5),
        Electronics(condition=1.2)
    ]

    condition_a = items[0].condition_description()
    condition_b = items[1].condition_description()
    condition_c = items[2].condition_description()
    condition_d = items[3].condition_description()

    assert condition_a == "Like new condition"
    assert condition_b == "Very good condition"
    assert condition_c == "Good condition without noticeable wear and tear"
    assert condition_d == "Acceptable condition but noticeable wear and tear"
