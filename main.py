import sys
import os
from collections import defaultdict


def check_number_of_arguments():
    """Check number of entered arguments and return error to user if there are not 2 of them.
    Returns list of arguments."""

    number_of_arguments = len(sys.argv) - 1
    if number_of_arguments != 2:
        print("Check yours arguments. There should be input.txt and output.txt files.")
        exit()
    else:
        arguments = list(sys.argv[1:])
        return arguments


def check_existence_and_types_of_arguments(entered_arguments):
    """Takes list that consist of input and output files.
    Check that entered input file exist, not empty and both entered files have .txt type.
    Returns error to user if one of checks was failed.
    Returns list of arguments."""

    # Check that file exist
    input_file_existence = os.path.isfile(entered_arguments[0])
    if not input_file_existence:
        print(f"Impossible to open {entered_arguments[0]}. Please write file's name or it's path correctly.")
        exit()
    else:

        # Check that file is not empty
        if os.stat(entered_arguments[0]).st_size == 0:
            print(f"{entered_arguments[0]} is empty. Please fill it out.")
            exit()

        # Check that both files has .txt type
        for arg in entered_arguments:
            extension = os.path.splitext(arg)[1]
            if extension != ".txt":
                print(f"{arg} is not a .txt file. Input and output files should have .txt type")
                exit()

    return entered_arguments


def make_calculations(input_doc):
    """Takes input file.
    Open input file and for every line: check amount of numbers in line (if != 3, copy this line to list of
    broken lines), check that all symbols in line have integer type (if not copy this line to list of broken lines,
    create a loop for finding all multiples of both numbers which are below the third number, output is a list of all
    multiples (with duplicates), Crete a set to remove duplicates and create dict with format that will be comfortable
    for upcoming sorting (defaultdict) -
    {number_of_multiples: [[third number, [multiplies from line], [multiplies from another line], ...]]}.
    Returns - dict for sorting and list of broken lines."""

    # Open file for reading
    with open(input_doc, "r", encoding="utf-8") as input_file:
        output_dict = defaultdict(list)
        list_of_broken_lines = []

        # Going through every line
        for line in input_file.readlines():
            list_of_line_symbols = line.split()

            # Check amount of numbers, if != 3, copy this line in list of broken lines
            if len(list_of_line_symbols) != 3:
                output_error_0 = f"{line.strip()} - the number of elements in this line is not equal to 3"
                list_of_broken_lines.append(output_error_0)
            else:
                # Check that all numbers are integers, if not copy this line in list of broken lines
                try:
                    numbers_list = [int(list_of_line_symbols[0]), int(list_of_line_symbols[1])]
                    limit = int(list_of_line_symbols[2])
                except ValueError:
                    output_error_1 = f"{line.strip()} - some elements in the line are not integers"
                    list_of_broken_lines.append(output_error_1)
                    continue

                # Find all multiples of both numbers which are below the third number,
                # output - list of all multiples (with duplicates)
                multiples_list = []
                for number in numbers_list:
                    i = 1
                    while i*number < limit:
                        multiples_list.append(i*number)
                        i += 1

                # Crete a set to remove duplicates and create dict with format that will be comfortable
                # for upcoming sorting (defaultdict) -
                # {number_of_multiples: [[third number, [multiplies from line], [multiplies from another line], ...]]}
                multiples_set = sorted(set(multiples_list))
                number_of_multiples = len(multiples_set)
                one_line_info = [limit, multiples_set]
                output_dict[number_of_multiples].append(one_line_info)

    return output_dict, list_of_broken_lines


def write_calculations_in_file(calculations_dict, broken_str_list, output_doc):
    """
    Takes dict for sort, list of broken lines and output file.
    Doesn't check existence of output file from user - can create it by itself.
    Open output file, sort the number of multiples and goes through every item of defaultdict, goes through every
    multiples list (if there are duplicated third numbers) of every third number, creates output line, print it to
    console and write to output file, print to console and write to file all broken lines.
    Returns nothing - print output to console and to output file."""

    # Open file for writing (if file already exist, program will rewrite it)
    with open(output_doc, "w", encoding="utf-8") as output_file:

        # Sort the number of multiples and goes through every item of defaultdict
        for amount_of_multiples, info_list in sorted(calculations_dict.items()):
            # Goes through every multiples list (if there are duplicated third numbers) of every third number, creates
            # output line, print it to console and write to output file
            for one_info_list in info_list:
                output_str = ""
                for one_elem in one_info_list[1]:
                    output_str += str(one_elem) + " "
                print(f"{one_info_list[0]}:{output_str}")
                output_file.write(f"{one_info_list[0]}:{output_str}\n")

        # print to console and write to file all broken lines
        for broken_str in broken_str_list:
            output_file.write(f"{broken_str}\n")
            print(broken_str)


if __name__ == "__main__":
    user_arguments = check_number_of_arguments()
    correct_arguments = check_existence_and_types_of_arguments(user_arguments)
    calculated_dict, broken_lines_list = make_calculations(correct_arguments[0])
    write_calculations_in_file(calculated_dict, broken_lines_list, correct_arguments[1])

