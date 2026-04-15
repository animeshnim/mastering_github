def custom_reverse(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return string[:i] + string[i:][::-1]




if __name__ == '__main__':
    input_str = input("Enter a styring for custom input: ")
    input_chr = input("Reverse Character: ")

    print("The output is ", end="")
    print('"', custom_reverse(input_str, input_chr), '"', sep="")
