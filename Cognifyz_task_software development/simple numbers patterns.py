def right_angled_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def number_pyramid(rows):
    for i in range(1, rows + 1):
        print("  " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()


def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print("  " * (rows - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()


def floyds_triangle(rows):
    num = 1
    for i in range(1, rows + 1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()


def repeating_number_triangle(rows):
    for i in range(1, rows + 1):
        for _ in range(i):
            print(i, end=" ")
        print()


def display_menu():
    print("\nNUMBER PATTERN GENERATOR")
    print("1. Right-Angled Number Triangle")
    print("2. Centered Number Pyramid")
    print("3. Inverted Number Pyramid")
    print("4. Floyd's Triangle")
    print("5. Repeating Number Triangle")
    print("6. Generate All Patterns")
    print("7. Exit")


def get_valid_rows():
    while True:
        try:
            rows = int(input("Enter number of rows: "))
            if 1 <= rows <= 25:
                return rows
            print("Enter a number between 1 and 25.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice.")
            continue

        rows = get_valid_rows()

        if choice == "1":
            right_angled_triangle(rows)
        elif choice == "2":
            number_pyramid(rows)
        elif choice == "3":
            inverted_pyramid(rows)
        elif choice == "4":
            floyds_triangle(rows)
        elif choice == "5":
            repeating_number_triangle(rows)
        elif choice == "6":
            right_angled_triangle(rows)
            number_pyramid(rows)
            inverted_pyramid(rows)
            floyds_triangle(rows)
            repeating_number_triangle(rows)

        run_again = input("\nTry another pattern? (Y/N): ").strip().lower()
        if run_again not in ["y", "yes"]:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()