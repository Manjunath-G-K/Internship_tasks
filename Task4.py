# Task 4: Build a temperature converter program.
# Student: Manjunath G K
# Date: 10/09/2025


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def main():


    while True:
        print("\n===== Temperature Converter =====")
        print("1. Celsius ➝ Fahrenheit")
        print("2. Fahrenheit ➝ Celsius")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F")

        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")

        elif choice == "3":
            print("Exiting Temperature Converter. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

