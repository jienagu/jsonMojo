import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jsonMojo.tidy_dict import remove_element

test_dict = {
    "A": "1",
    "B": "2",
    "C":{
        "C1": ["1", "45"]
    }
}

def test_remove_element():
    assert remove_element(test_dict, to_remove = "1" ) == {'B': '2', 'C': {'C1': ['45']}}, "Should be {'B': '2', 'C': {'C1': ['45']}}!"


if __name__ == "__main__":
    test_remove_element()
    print("test_remove_element() passed")
