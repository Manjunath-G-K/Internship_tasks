# Task 2: Generate and print simple number patterns.
# Student: Manjunath G K
# Date: 08/09/2025

# function 1: Right-Angled Triangle Pattern
def right_angled_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# Function 2: Pyramid Pattern
def pyramid_pattern(n):
    for i in range(1, n+1):
        print(" " * (n - i), end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Function 3: Inverted Pyramid Pattern
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i+1):
            print(j, end=" ")
        print()

# Main function to call all patterns
def main():
    n = int(input("Enter number of rows: "))

    print("\n--- Right-Angled Triangle Pattern ---")
    right_angled_triangle(n)

    print("\n--- Pyramid Pattern ---")
    pyramid_pattern(n)

    print("\n--- Inverted Pyramid Pattern ---")
    inverted_pyramid(n)

#calling main function
main()
