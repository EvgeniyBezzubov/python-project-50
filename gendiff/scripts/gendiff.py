import argparse
import json


def main():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compares two configuration '
                                                 'files and shows a '
                                                 'difference.',
                                     epilog="          And that's how "
                                            "you'd foo a bar")

    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    generate_diff(args.first_file, args.second_file)


def generate_diff(path1, path2):
    """
    --Whats is it
    --Tomato sauce
    --... Why
    --For you spaghetti code
    """

    first_file = json.load(open(path1))
    sorted_first_file_dict = dict(sorted(first_file.items()))

    second_file = json.load(open(path2))

    sorted_second_file_dict = dict(sorted(second_file.items()))
    ans_dict = {}
    for i in sorted_first_file_dict:
        if i in sorted_second_file_dict:
            if sorted_first_file_dict[i] == sorted_second_file_dict[i]:
                ans_dict[i] = sorted_first_file_dict[i]
                sorted_second_file_dict.pop(i)
            else:
                ans_dict["- " + i] = sorted_first_file_dict[i]
                ans_dict["+ " + i] = sorted_second_file_dict[i]
                sorted_second_file_dict.pop(i)
        else:
            ans_dict["- " + i] = sorted_first_file_dict[i]

    for i in sorted_second_file_dict:
        ans_dict["+ " + i] = sorted_second_file_dict[i]
    return str(ans_dict)


if __name__ == "__main__":
    main()
