from functions.level_1.three_url_builder import build_url


def test_build_url_without_query_params():
    assert build_url('https://example.com', 'path/to/resource') == 'https://example.com/path/to/resource'

def test_build_url_with_query_params():
    assert build_url('https://example.com', 'path/to/resource', {'key1': 'value1', 'key2': 'value2'}) == 'https://example.com/path/to/resource?key1=value1&key2=value2'

def test_build_url_with_single_query_param():
    assert build_url('https://example.com', 'path/to/resource', {'key1': 'value1'}) == 'https://example.com/path/to/resource?key1=value1'

def test_build_url_with_empty_query_params():
    assert build_url('https://example.com', 'path/to/resource', {}) == 'https://example.com/path/to/resource'

def test_build_url_with_no_query_params():
    assert build_url('https://example.com', 'path/to/resource', None) == 'https://example.com/path/to/resource'

def test_build_url_with_special_characters():
    assert build_url('https://example.com', 'path/to/resource', {'key1': 'value with spaces', 'key2': 'value&with:special?chars'}) == 'https://example.com/path/to/resource?key1=value with spaces&key2=value&with:special?chars'   

def test_build_url_with_tailing_slash_in_relative_url():
    assert build_url('https://example.com', 'path/to/resource/') == 'https://example.com/path/to/resource/'

def test_build_url_with_empty_relative_url():
    assert build_url('https://example.com', '') == 'https://example.com/'

def test_build_url_with_empty_hostname():
    assert build_url('', 'path/to/resource') == '/path/to/resource'