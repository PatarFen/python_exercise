import string
import random


def code_generator(code_len, num_of_code):
    all_chars = string.ascii_letters + string.digits
    result = " "
    code_list = []
    for _ in range(num_of_code):
        result = " "
        for _ in range(code_len):
            result = result + (random.choice(all_chars))
        while (result in code_list):
            for _ in range(code_len):
                result = result + (random.choice(all_chars))
        code_list.append(result)
    return code_list

result = code_generator(8,2000)
print(result)