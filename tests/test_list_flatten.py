import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jsonMojo.tidy_dict import list_flatten


def test_list_flatten():
    assert list_flatten(['2', ['1', '3', ['a', '1']]] ) == ['2', '1', '3', 'a', '1'], "Should be ['2', '1', '3', 'a', '1']!"


if __name__ == "__main__":
    test_list_flatten()
    print("test_list_flatten() passed")
