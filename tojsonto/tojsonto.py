import json
import csv

def object_to_csv_row(object, header, delim):
    row = []
    for col in header:
        row.append(object.get(col, ""))

    return delim.join(row)

def csv_row_to_object(row, header, delim):
    row_items = row.split(delim)
    obj = {}
    for i, col in enumerate(header):
        if row_items[i]:
            obj[col] = row_items[i]

    return obj

 
def find_csv_headers_from_list(json_list, prefix, header=set()):
    for i, value in enumerate(json_list):
        key = f"{i}"
        key_tree = []
        key_tree.extend(prefix)
        key_tree.append(key)
        if type(value) is dict:
            find_csv_headers_from_dict(value, key_tree, header=header)
        elif type(value) is list:
            find_csv_headers_from_list(value, key_tree, header=header)
        else:
            header.add(".".join(key_tree))    


def find_csv_headers_from_dict(json_obj, prefix=[], header=set()):
    for item in json_obj.items():
        key = str(item[0])
        value = item[1]
        key_tree = []
        key_tree.extend(prefix)
        key_tree.append(key)
        if type(value) is dict:
            find_csv_headers_from_dict(value, key_tree, header=header)
        elif type(value) is list:
            find_csv_headers_from_list(value, key_tree, header=header)
        else:
            header.add(".".join(key_tree))
        value = item[1]

def create_row(obj, header):
    row_dict = {}
    for col in header:
        cols = col.split('.')
        val = None
        o = obj
        for c in cols:
            try:
                if c.isnumeric():
                    c = int(c)
                o = o[c]
            except:
                o = None
        row_dict[col] = o

    return row_dict
        

def json_to_csv(input_file=None, output_file=None, auto_id=False, header=None):
    if input_file == None or output_file == None:
        # TODO raise exception
        return

    with open(input_file, "r") as input_file:
        input_json = json.load(input_file)
        if type(input_json) is not list:
            # TODO raise exception
            return

        header = set()
        for obj in input_json:
            find_csv_headers_from_dict(obj, header=header)

        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = sorted(list(header))
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for obj in input_json:
                row_dict = create_row(obj, header)
                writer.writerow(row_dict)

# def csv_to_json(input_file=None,
#                 output_file=None,
#                 header_detection=False,
#                 header=None):
#     pass