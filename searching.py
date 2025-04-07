import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    allowed_keyz = {"unordered_numbers","ordered_numbers","dna_sequence"}
    if field not in allowed_keyz:
        return None

    with open(file_path, mode="r") as f:
        data=json.load(f)


    return data[field]
def main():
    print(read_data("sequential.json", "unordered_numbers"))


if __name__ == '__main__':
    main()