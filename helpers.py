import math

def read_file_to_list(file_name):
    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        return [l.strip('\n\r') for l in lines]

def check_consistency(data):
        if any(word in data for word in computer_specific_words):
            return 'computer-mouse'
        else:
            return 'animal'

computer_specific_words = ['device', 'input', 'computer', 'ergonomic', 'wireless', 'USB', 'gaming',
    'roll', 'razer', 'DeathAdder', 'dpi', 'optical', 'sensor', 'mobile', 'phone', 'tablet', 'wireless',
    'keyboard', 'click', 'button', 'display', 'screen']