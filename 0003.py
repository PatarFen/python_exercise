import string
import random
import redis

def insert_promote_code(code):
    id = random.getrandbits(32)
    code = code
    r = redis.Redis()
    r.set(id,code)

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
        #random.seed(777)
        insert_promote_code(result)
        
    #return code_list
    print("codes generation is done~")

if __name__ == "__main__":
    code_generator(5,6)