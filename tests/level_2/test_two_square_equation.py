from functions.level_2.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, -3, 2, (1.0, 2.0)),
        (2, -3, -5, (-1.0, 2.5)),
    ],
)
def test__solve_square_equation__discriminant_greater_that_zero_results_in_two_roots(
    a, b, c, expected
):
    assert solve_square_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 4, 4, (-2.0, -2.0)),
        (1, -2, 1, (1.0, 1.0)),
    ],
)
def test__solve_square_equation__discriminant_equal_to_zero_results_in_one_root(
    a, b, c, expected
):
    assert solve_square_equation(a, b, c) == expected


def test__solve_square_equation__linear_equation_results_in_one_root():
    assert solve_square_equation(0, 2, -4) == (2.0, None)


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 0, 1, (None, None)),
        (0, 0, 5, (None, None)),
    ],
)
def test__solve_square_equation__discriminant_less_than_zero_results_in_no_root(
    a, b, c, expected
):
    assert solve_square_equation(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (0, 0, 0, (None, None)),
        (0, 0, -1, (None, None)),
    ],
)
def test__solve_square_equation__incorrect_coefficients_results_in_no_root(
    a, b, c, expected
):
    assert solve_square_equation(a, b, c) == expected
