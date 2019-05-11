from helpers import read_file_to_list, check_consistency, computer_specific_words

tested_files_dict = {
    "data/input00.txt": "data/output00.txt",
    "data/input01.txt": "data/output01.txt"
}

for key in tested_files_dict:

    input_data = read_file_to_list(key)
    output_data = read_file_to_list(tested_files_dict[key])
    count = int(input_data.pop(0))
    
    for i in range(0, count):
        result = check_consistency(input_data[i])
        print(result, output_data[i])
        assert result == output_data[i], "Inconsistency in line {0} of output file {1}." .format(i+1, tested_files_dict[key])
