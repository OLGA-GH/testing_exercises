from functions.level_1.five_title import change_copy_item
import pytest

testdata = [
    ('My Document', 'Copy of My Document'),
    ('Copy of My Document', 'Copy of My Document (2)'),
    ('Copy of My Document (1)', 'Copy of My Document (2)'),
    ('Copy of My Document (2)', 'Copy of My Document (3)'),
    ('Copy of My Document (9)', 'Copy of My Document (10)'),
    ('A' * 91, 'Copy of ' + 'A' * 91), # len < max_main_item_title_length
    ('A' * 92, 'A' * 92), # len == max_main_item_title_length
    ('A' * 93, 'A' * 93), # len > max_main_item_title_length
]

@pytest.mark.parametrize("title, expected", testdata)
def test_change_copy_item(title, expected):
    assert change_copy_item(title) == expected
