import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jsonMojo.tidy_dict import filter_rowwise

input_rowwise = [
    {"id": 10, "dept": "Biology"},
    {"id": 2, "dept": "Chemistry"},
    {"id": 3, "dept": "Computer Science"}
]

def test_filter_rowwise():
    assert filter_rowwise(input_rowwise, by_key = "dept", filter_in = ["Biology", "Computer Science"]) == [{'id': 10, 'dept': 'Biology'}, {'id': 3, 'dept': 'Computer Science'}], "Should be [{'id': 10, 'dept': 'Biology'}, {'id': 3, 'dept': 'Computer Science'}]!"


if __name__ == "__main__":
    test_filter_rowwise()
    print("test_filter_rowwise() passed")
