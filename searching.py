import os
import json
from operator import index

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

def linear_search(seq_search, number):
    count  = 0
    positions = []
    for idx, i in enumerate(seq_search):
        if i == number:
            count = count+1
            positions.append(idx)
    result = {"positions":positions,"count":count}
    return result


def pattern_search(seq_search, pattern):
    length = len(pattern)
    sequence = len(seq_search)
    i = 0
    positions = set()
    while i < sequence - length:
        if seq_search[i:i+length] == pattern:
            positions.add(i + length // 2)
        i=i+1
    return positions


def main():
    seq_search = read_data("sequential.json", "dna_sequence")
    print(pattern_search(seq_search, "ATA"))

if __name__ == '__main__':
    main()