import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jsonMojo.tidy_dict import sort_rowwise

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def test_sort_rowwise():
    assert sort_rowwise(cars, by_key = 'car', descending =False) == \
        [{'car': 'BMW', 'year': 2019},
 {'car': 'Ford', 'year': 2005},
 {'car': 'Mitsubishi', 'year': 2000},
 {'car': 'VW', 'year': 2011}], "Should be [{'car': 'BMW', 'year': 2019},{'car': 'Ford', 'year': 2005},{'car': 'Mitsubishi', 'year': 2000},{'car': 'VW', 'year': 2011}]!"


if __name__ == "__main__":
    test_sort_rowwise()
    print("test_sort_rowwise() passed")
