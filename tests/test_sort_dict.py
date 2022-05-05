import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jsonMojo.tidy_dict import sort_dict



def test_sort_dict():
    assert sort_dict(input_dict = {"A": 2, "BA": 4, "GW": 3, "EW": 1, "W": 0}, sort_by_key = False) == {'W': 0, 'EW': 1, 'A': 2, 'GW': 3, 'BA': 4}, "Should be {'W': 0, 'EW': 1, 'A': 2, 'GW': 3, 'BA': 4}!"


if __name__ == "__main__":
    test_sort_dict()
    print("test_sort_dict() passed")
