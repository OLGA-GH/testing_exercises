from functions.level_1.two_date_parser import compose_datetime_from
import datetime
import pytest

testdata_positive = [
    ('today', '23:59', datetime.datetime.strptime(f'{datetime.date.today()} 23:59:00', "%Y-%m-%d %H:%M:%S")),
    ('tomorrow', '23:59', datetime.datetime.strptime(f'{datetime.date.today() + datetime.timedelta(days=1)} 23:59:00', "%Y-%m-%d %H:%M:%S")),
    ('', '00:00', datetime.datetime.strptime(f'{datetime.date.today()} 00:00:00', "%Y-%m-%d %H:%M:%S")),
    (None, '01:05', datetime.datetime.strptime(f'{datetime.date.today()} 01:05:00', "%Y-%m-%d %H:%M:%S")),
]

testdata_negative = [
    ('today', '23', pytest.raises(ValueError)),
    ('today', ':23', pytest.raises(ValueError)),
    ('today', '23:', pytest.raises(ValueError)),
    ('today', ':', pytest.raises(ValueError)),
    ('today', '00:00:00', pytest.raises(ValueError)),
    ('today', None, pytest.raises(AttributeError)),
]

@pytest.mark.parametrize("date_str, time_str, expectation", testdata_positive)
def test_compose_datetime_from_positive(date_str, time_str, expectation):
    assert compose_datetime_from(date_str, time_str) == expectation

@pytest.mark.parametrize("date_str, time_str, expectation", testdata_negative)
def test_compose_datetime_from_negative(date_str, time_str, expectation):
    with expectation:
        compose_datetime_from(date_str, time_str)