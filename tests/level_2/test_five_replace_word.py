from functions.level_2.five_replace_word import replace_word
import pytest


def test__replace_word__replaces_existant_word_succesfuly():
    assert replace_word("Hello world", "world", "all") == "Hello all"


def test__replace_word__allows_multiple_replacement():
    assert replace_word("world Hello world", "world", "hi") == "hi Hello hi"


@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected",
    [
        (
            "hello hello hello",
            "HELLO",
            "hi",
            "hi hi hi",
        ),
        (
            "hello Hello HELLO",
            "hello",
            "hi",
            "hi hi hi",
        ),
    ],
)
def test__replace_word__replace_in_different_cases_allowed(
    text, replace_from, replace_to, expected
):
    assert replace_word(text, replace_from, replace_to) == expected


def test__replace_word__no_replacement_if_word_not_exist():
    assert replace_word("Hello world", "Hi", "Bye") == "Hello world"


def test__replace_word__no_replacement_if_replace_from_is_empty():
    assert replace_word("Hello world", "", "Bye") == "Hello world"


def test__replace_word__replacement_if_replace_to_is_empty():
    assert replace_word("Hello world", "world", "") == "Hello "


def test__replace_word__replaces_with_punctuation_succesfuly():
    assert replace_word("Hello world.", "world.", "world!") == "Hello world!"


def test__replace_word__returns_empty_string_if_text_is_empty():
    assert replace_word("", "world", "world!") == ""


def test__replace_word__replaces_word_in_single_word_sentence_sucessfully():
    assert replace_word("Hi", "Hi", "Hello") == "Hello"
