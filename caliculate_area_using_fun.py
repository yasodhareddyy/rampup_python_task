import math

def calculate_area(*args):
    if len(args) == 2:
        length, width = args
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative")
        print("This is the rectangle method")
        return f"The rectangle area value is {length * width}"
    elif len(args) == 1:
        radius = args[0]
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        print("This is the circle method")
        return f"The circle area value is {math.pi * radius ** 2}"
    elif len(args) == 3 and args[2] == 'triangle':
        base, height = args[:2]
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative")
        print("This is the triangle method")
        return f"The triangle area value is {0.5 * base * height}"
    else:
        raise ValueError("Invalid arguments provided")

while True:
    try:
        print("Choose any one to calculate the area:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")

        choice = int(input("Enter the number of your choice (1, 2, or 3): "))

        if choice == 1:
            length = float(input("Enter length value of the rectangle: "))
            width = float(input("Enter width value of the rectangle: "))
            print(calculate_area(length, width))
        elif choice == 2:
            radius = float(input("Enter radius value: "))
            print(calculate_area(radius))
        elif choice == 3:
            base = float(input("Enter the base value of the triangle: "))
            height = float(input("Enter the height value of the triangle: "))
            shape = input("Enter 'triangle' for the shape: ")
            print(calculate_area(base, height, shape))
        else:
            print("Please select a valid option (1, 2, or 3).")
            continue

    except ValueError as e:
        print(f"Error: {e}. Please provide correct values.")
    except Exception as ex:
        print(f"An error occurred: {ex}")

    choice = input("Do you want to calculate another area? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting the program.")
        break
