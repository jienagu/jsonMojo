import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jsonMojo.tidy_dict import replace_element

test_dict = {
    "A": "1",
    "B": "2",
    "C":{
        "C1": ["1", "45"]
    }
}

def test_replace_element():
    assert replace_element(test_dict, to_replace = "1", replace_with = "A1" ) == {'A': 'A1', 'B': '2', 'C': {'C1': ['A1', '45']}}, "Should be {'A': 'A1', 'B': '2', 'C': {'C1': ['A1', '45']}}!"


if __name__ == "__main__":
    test_replace_element()
    print("test_replace_element() passed")
