from collections import deque


def extending_string(string: str, number: int) -> str:
    s_deque = deque(string)
    counter = 0
    while len(s_deque) != number and len(s_deque) < number+1:
        if counter == 0:
            s_deque.extend(" ")
            counter = counter + 1
        elif counter == 1:
            s_deque.extendleft(" ")
            counter = counter + 1
        else:
            if len(s_deque) % 2 == 0:
                s_deque.extend("#")
            s_deque.extendleft("#")
    return_string  = "".join(s_deque)
    return return_string+"#" if len(return_string) < number+1 else return_string

def clean_log(string:str, number: int) -> str:
    if len(string) > number:
        string_as_list = string.split(" ")
        return_string = ""
        for batch_string in string_as_list:
            return_string = return_string + extending_string(batch_string, number)
            return_string = return_string + "\n"
        return return_string
    else:
        return extending_string(string, number)

def log_print(*args) -> None:
    # check args list or strings
    print("<^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^>")
    print("###################################################")
    print("################## PRETTY LOGGER ##################")
    long_string = ""
    #import ipdb;ipdb.set_trace()
    for a in args:
        long_string = long_string + " " + "".join(str(a))
    print(clean_log(long_string, 50))
    print("###################################################")
    print("###################################################")
    print("<_________________________________________________>")
