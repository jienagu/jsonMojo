## jsonMojo 
[![Downloads](https://static.pepy.tech/personalized-badge/jsonmojo?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)](https://pepy.tech/project/jsonmojo)

A series of utility functions to help with tidy json via python dictionary.

## Installation from github
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install jsonMojo.

```
pip install jsonMojo
```

## features

* `replace_element`: recursively replace an element by a desired element within a dictionary
* `remove_element`: recursively remove a desired element within a dictionary
* `list_flatten`: recursively flat a list/array
* `sort_dict`: sort a python dictionary by either key or value
* `filter_rowwise`: filter a rowwise list/array by selected value(s)
* `sort_rowwise`: sort a rowwise list/array by selected key


## Usage

```python
import jsonMojo as jm

# test_dict as an example input
test_dict = {
    "A": "1",
    "B": "2",
    "C":{
        "C1": ["1", "45"]
    }
}
```

### Recursively replace an element by a desired element within a dictionary

```python
jm.replace_element(test_dict, to_replace = "1", replace_with = "A1" )
#returns {'A': 'A1', 'B': '2', 'C': {'C1': ['A1', '45']}}
```
We can set `output_json = True` if we want the output in JSON string format.

```python
jm.replace_element(test_dict, to_replace = "1", replace_with = "A1" , output_json = True)
#returns '{\n"A": "A1",\n"B": "2",\n"C": {\n"C1": [\n"A1",\n"45"\n]\n}\n}'}
```

### Recursively remove a desired element within a dictionary

```python
jm.remove_element(test_dict, to_remove = "1" )
#returns {'B': '2', 'C': {'C1': ['45']}}
```

```python
jm.remove_element(test_dict, to_remove = "1" , output_json = True)
#returns '{\n"B": "2",\n"C": {\n"C1": [\n"45"\n]\n}\n}'
```

### recursively flat a list/array

```python
jm.list_flatten(['2', ['1', '3', ['a', '1']]] )
#returns ['2', '1', '3', 'a', '1']

jm.list_flatten(list({"A", "B"}))
#returns ['A', 'B']
```

```python
jm.list_flatten(['2', ['1', '3', ['a', '1']]] , output_json = True)
#returns '[\n"2",\n"1",\n"3",\n"a",\n"1"\n]'

jm.list_flatten(list({"A", "B"}), output_json = True)
#returns '[\n"A",\n"B"\n]'
```

### sort a python dictionary by either key or value

```python
jm.sort_dict(input_dict = {"A": 2, "BA": 4, "GW": 3, "EW": 1, "W": 0}, sort_by_key = False, descending = False )
# returns {'W': 0, 'EW': 1, 'A': 2, 'GW': 3, 'BA': 4}

jm.sort_dict(input_dict = {"A": 2, "BA": 4, "GW": 3, "EW": 1, "W": 0}, sort_by_key = True, descending = False )
# returns {'A': 2, 'BA': 4, 'EW': 1, 'GW': 3, 'W': 0}
```
We can set `output_json = True` if we want the output in JSON string format.

### filter a rowwise list/array by selected value(s)

```python
input_rowwise = [
    {"id": 10, "dept": "Biology"},
    {"id": 2, "dept": "Chemistry"},
    {"id": 3, "dept": "Computer Science"}
]
jm.filter_rowwise(input_rowwise, by_key = "dept", filter_in = ["Biology", "Computer Science"])
# returns [{'id': 1, 'dept': 'Biology'}, {'id': 3, 'dept': 'Computer Science'}]
```
We can set `output_json = True` if we want the output in JSON string format.

### sort a rowwise list/array by selected key

```python
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
jm.sort_rowwise(cars, by_key = 'car', descending =False)
# returns [{'car': 'BMW', 'year': 2019},
# {'car': 'Ford', 'year': 2005},
# {'car': 'Mitsubishi', 'year': 2000},
# {'car': 'VW', 'year': 2011}]
```
We can set `output_json = True` if we want the output in JSON string format.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
