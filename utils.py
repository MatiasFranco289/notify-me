def write_env(var_name, var_value) -> None:

    try:
        with open(".env", "r") as file:
            lines = file.readlines()
    except:
        print("Error while opening .env file")
        exit(1)
    
    try:
        with open(".env", "w") as file:
            for line in lines:
                if var_name in line:
                    file.write(var_name + " = " + var_value + "\n")
                else:
                    file.write(line)
    except:
        print("Error while writing .env file")
        exit(1)

def get_tuple_difference(tuple1, tuple2) -> float:
    difference = 0
    for i in range(len(tuple1)):
        difference += abs(tuple1[i] - tuple2[i])
    return difference