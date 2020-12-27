import json
import utils


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


def json_to_csv(input_file=None, output_file=None, auto_id=False, header=None):
    if input_file == None or output_file == None:
        # TODO raise exception
        return

    with json.load(input_file) as input_json:
        if type(input_json) is not list:
            # TODO raise exception
            return

        if not header:
            # TODO get all possible headers from json
            pass

        save_as_csv()

        pass

    pass


def csv_to_json(input_file=None,
                output_file=None,
                header_detection=False,
                header=None):
    pass