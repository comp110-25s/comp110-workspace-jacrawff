"Testing the Dictionary"

__author__: str = "730649503"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_basic():
    """Basic test for invert function."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair():
    """Single key-value pair inversion."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_key_error():
    """Test invert function raises KeyError on duplicate values."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


def test_count_basic():
    """Basic count test."""
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_count_unique():
    """Test count function with all unique items."""
    assert count(["a", "b", "c"]) == {"a": 1, "b": 1, "c": 1}


def test_count_empty():
    """Test count function with an empty list."""
    assert count([]) == {}


def test_favorite_color_basic():
    """Basic test for favorite_color function."""
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Charlie": "red"}) == "blue"


def test_favorite_color_tie():
    """Test favorite_color function with a tie."""
    assert favorite_color({"Alice": "red", "Bob": "blue"}) in {"red", "blue"}


def test_favorite_color_single():
    """Test favorite_color function with a single entry."""
    assert favorite_color({"Alice": "green"}) == "green"


def test_bin_len_basic():
    """Basic test for bin_len function."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_duplicates():
    """Test bin_len function with duplicate words."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty():
    """Test bin_len function with an empty list."""
    assert bin_len([]) == {}
