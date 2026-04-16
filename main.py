def custom_reverse(string, char):
    i = string.index(char)
    return string[:i] + string[i:][::-1]


def check_palindrome(string):
    reverse_str = string[::-1]
    
    if (string == reverse_str):
        return True
    else:
        return False



if __name__ == '__main__':
    input_str = input("Enter a styring for custom input: ")
    input_chr = input("Reverse Character: ")

    print("The output is ", end="")
    print('"', custom_reverse(input_str, input_chr), '"', sep="")


    input_str = input("String to check Palindrome: ")
    print("The output is ", end="")
    print('"', check_palindrome(input_str), '"', sep="")
