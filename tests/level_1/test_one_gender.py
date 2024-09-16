from functions.level_1.one_gender import genderalize
import pytest

testdata = [
    ('verb_male', 'verb_female', 'male', 'verb_male'),
    ('verb_male', 'verb_female', 'female', 'verb_female'),
    ('verb_male', 'verb_female', 'Male', 'verb_female'),
    ('verb_male', 'verb_female', 'malee', 'verb_female'),
    ('verb_male', 'verb_female', '', 'verb_female'),
    ('verb_male', 'verb_female', 123, 'verb_female'),
]

@pytest.mark.parametrize("verb_male, verb_female, gender, expected", testdata)
def test_genderalize(verb_male, verb_female, gender, expected):
    assert genderalize(verb_male, verb_female, gender) == expected
