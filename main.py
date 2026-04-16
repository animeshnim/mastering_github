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


def check_palindrome(string):
    reverse_str = string[::-1]
    
    if (string == reverse_str):
        return True
    else:
        return False


if __name__ == '__main__':
    # Choice Screen:
    print("Choose the functionality you want to use")
    print("1. Reverse Second Half of the String at a Char")
    print("2. Compress the String")
    print("3. Check Palindrome")
    func_to_run = int(input("Enter your choice (only numbers are allowed): "))

    if (func_to_run == 1):
        input_str = input("Enter a styring for custom input: ")
        input_chr = input("Reverse Character: ")
        print("The output is ", end="")
        print('"', custom_reverse(input_str, input_chr), '"', sep="")
    
    elif (func_to_run == 2):
        input_str = input("String to compress: ")
        print("The compressed string is ", end="")
        print('"', string_compress(input_str), '"', sep="")

    
    elif (func_to_run == 3):
        input_str = input("Enter String to Check Palindrome: ")
        output = check_palindrome(input_str)
        if (output == True):
            print("The string is a palindrome string")
        else:
            print("The string is not a palindrome string")