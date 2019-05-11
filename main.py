from helpers import read_file_to_list, check_consistency, computer_specific_words

def main():
    data = read_file_to_list("data/input01.txt")
    count = int(data.pop(0))
    for i in range(0, count):
        print(check_consistency(data[i]))
            

if __name__ == "__main__":
    main()