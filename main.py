def custom_reverse(string, char):
    i = string.index(char)
    return string[:i] + string[i:][::-1]


def string_compress(string):
    result_str = ""
    count = 1

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            count += 1
        else:
            result_str = result_str + string[i - 1] + str(count)
            count = 1
    
    result_str = result_str + string[i] + str(count)
    
    return result_str


if __name__ == '__main__':
    # Choice Screen:
    print("Choose the functionality you want to use")
    print("1. Reverse Second Half of the String at a Char")
    print("2. Compress the String")
    func_to_run = input("Enter your choice (only numbers are allowed): ")

    if (func_to_run == 1):
        input_str = input("Enter a styring for custom input: ")
        input_chr = input("Reverse Character: ")

        print("The output is ", end="")
        print('"', custom_reverse(input_str, input_chr), '"', sep="")
    

    elif (func_to_run == 1):
        input_str = input("String to compress: ")
        print("The compressed string is ", end="")
        print('"', string_compress(input_str), '"', sep="")
