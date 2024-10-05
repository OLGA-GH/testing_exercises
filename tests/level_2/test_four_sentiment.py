from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
    "text, good_words, bad_words",
    [
        (
            "test happy 123",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "happy great good sad bad",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "GOOD",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "GOOD",
            {"happy", "great", "good"},
            {},
        ),
    ],
)
def test__check_tweet_sentiment__with_good_words_predominance_returns_GOOD(
    text, good_words, bad_words
):
    assert check_tweet_sentiment(text, good_words, bad_words) == "GOOD"


@pytest.mark.parametrize(
    "text, good_words, bad_words",
    [
        (
            "sad test 123",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "sad bad unhappy happy great",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "SAD",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "SAD",
            {},
            {"sad", "bad", "unhappy"},
        ),
    ],
)
def test__check_tweet_sentiment__with_bad_words_predominance_returns_BAD(
    text, good_words, bad_words
):
    assert check_tweet_sentiment(text, good_words, bad_words) == "BAD"


@pytest.mark.parametrize(
    "text, good_words, bad_words",
    [
        (
            "greater",  # 0 count
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "happy great good sad bad unhappy",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
    ],
)
def test__check_tweet_sentiment__with_equal_count_bad_and_good_words_returns_None(
    text, good_words, bad_words
):
    assert check_tweet_sentiment(text, good_words, bad_words) is None


@pytest.mark.parametrize(
    "text, good_words, bad_words",
    [
        (
            "sad but true",
            {},
            {},
        ),
        (
            "",
            {"happy", "great", "good"},
            {"sad", "bad", "unhappy"},
        ),
        (
            "",
            {},
            {},
        ),
    ],
)
def test__check_tweet_sentiment__with_empty_text_or_words_returns_None(
    text, good_words, bad_words
):
    assert check_tweet_sentiment(text, good_words, bad_words) is None
