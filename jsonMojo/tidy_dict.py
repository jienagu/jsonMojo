import json
def replace_element(d, to_replace, replace_with, output_json=False, indent = 0):
    """recursively replace an element by a desired element within a dictionary"""

    def find_search(x):
        return x == to_replace

    if not isinstance(d, (dict, list)):
        output = d
    elif isinstance(d, list):
        output = [v if not find_search(v) else replace_with for v in (replace_element(v, to_replace, replace_with) for v in d) ]
    
    else:
        output = {k: v if not find_search(v) else replace_with for k, v in ((k, replace_element(v, to_replace, replace_with)) for k, v in d.items()) }
    
    if(output_json):
        result = json.dumps(output, indent = indent)
    else:
        result = output
    
    return result


def remove_element(d, to_remove, output_json=False, indent = 0):
    """recursively remove a desired element from a dictionary"""

    def find_search(x):
        return x == to_remove

    if not isinstance(d, (dict, list)):
        output = d
    elif isinstance(d, list):
        output = [v for v in (remove_element(v, to_remove) for v in d) if not find_search(v)]

    else:
        output = {k: v for k, v in ((k, remove_element(v, to_remove)) for k, v in d.items()) if not find_search(v)}
    
    if(output_json):
        result = json.dumps(output, indent = indent)
    else:
        result = output
    
    return result


def list_flatten(input_list, output_json=False, indent = 0):
    '''Recursively flatten a list'''
    results = list()
    if isinstance(input_list, list):
        for each in input_list:
            results.extend(list_flatten(each))
    else:
        results.append(input_list)

    if(output_json):
        output = json.dumps(results, indent = indent)
    else:
        output = results
    return output


def sort_dict(input_dict, sort_by_key = True, descending = False , output_json=False, indent = 0):
    '''sort a dictionary by either keys or values'''
    if(sort_by_key):
        dict_output = {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[0], reverse= descending) }
    else:
        dict_output = {k: v for k, v in sorted(input_dict.items(), key=lambda item: item[1], reverse= descending) }
    if(output_json):
        output = json.dumps(dict_output, indent = indent)
    else:
        output = dict_output
    return output


def filter_rowwise(input_dict, by_key, filter_in , output_json=False, indent = 0):
    dict_output = [x for x in input_dict if x[by_key] in filter_in]
    if(output_json):
        output = json.dumps(dict_output, indent = indent)
    else:
        output = dict_output
    return output

def sort_rowwise(input_dict, by_key, descending = False, output_json=False, indent = 0):
    def sort_by(list):
        return list[by_key]
 
    input_dict.sort(key=sort_by, reverse= descending)
    
    if(output_json):
        output = json.dumps(input_dict, indent = indent)
    else:
        output = input_dict
    return output




