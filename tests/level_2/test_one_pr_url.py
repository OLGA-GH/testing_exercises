from functions.level_2.one_pr_url import is_github_pull_request_url
import pytest


@pytest.mark.parametrize(
    "url",
    (
        "https://github.com/OLGA-GH/testing_exercises/pull/1",
        "http://github.com/OLGA-GH/testing_exercises/pull/1",
    ),
)
def test__is_github_pull_request_url__with_valid_url_returns_true(url):
    assert is_github_pull_request_url(url)


@pytest.mark.parametrize(
    "url",
    (
        "https://gitlab.com/OLGA-GH/testing_exercises/pull/1",
        "https://github.com/OLGA-GH/testing_exercises/push/1",
        "https://github.com/OLGA-GH/testing_exercises/push/1/1",
        "https://github.com/OLGA-GH/testing_exercises/pulll/1",
        "https://github.ru/OLGA-GH/testing_exercises/pulll/1",
        "https://git/OLGA-GH/testing_exercises/pull/1",
        "https://github.com/OLGA-GH/testing_exercises/pull",
        "https://github.com/OLGA-GH/testing_exercises//1",
    ),
)
def test__is_github_pull_request_url__with_invalid_url_returns_false(url):
    assert not is_github_pull_request_url(url)


@pytest.mark.parametrize(
    "url",
    (
        "",
        " ",
        "123",
        "test",
        "//////",
    ),
)
def test__is_github_pull_request_url__with_malformed_url_returns_false(url):
    assert not is_github_pull_request_url(url)
