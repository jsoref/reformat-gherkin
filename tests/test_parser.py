import pytest

from main.errors import InvalidInput
from main.parser import parse


def test_invalid_input(invalid_contents):
    for content in invalid_contents:
        with pytest.raises(InvalidInput):
            parse(content)


def test_valid_input(valid_contents):
    for content in valid_contents():
        parse(content)
