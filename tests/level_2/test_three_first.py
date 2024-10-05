from functions.level_2.three_first import first
import pytest


@pytest.mark.parametrize(
    "item",
    (
        [1, 2, 3],
        [-1, -2, -3],
        [0],
    ),
)
def test__first__returns_first_element_for_non_empty_list(item):
    assert first(item) == item[0]

def test__first__with_empty_list_and_no_default_value_raises_attr_error():
    with pytest.raises(AttributeError):
        first([])

@pytest.mark.parametrize(
    "default_value",
    (
        -1,
        0,
        12345,
        None,
        "default_value"
    ),
)
def test__first__with_empty_list_and_default_value(default_value):
    assert first([], default=default_value) == default_value