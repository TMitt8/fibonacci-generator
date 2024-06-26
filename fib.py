'''
Fibonacci Number Generator
Cantor
Tanush Mittal
'''


def main():  
    # Takes in user input, prints n fibonacci numbers
    num_terms = input("Enter number of Fibonacci terms: ")
    # checks if input is valid
    valid = num_terms.isnumeric()

    if valid:
        num_terms = int(num_terms)
        a, b = 1, 1
        for i in range(0, num_terms):
            print(a)
            a, b = b, a+b
            i += 1
    else:
        print("Invalid input. Input must be a numeric value.")


if __name__ == "__main__":
    main()

