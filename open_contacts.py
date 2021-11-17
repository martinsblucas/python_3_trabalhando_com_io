import os


def main():
    print("********************************************")
    print("Readlines")
    print("********************************************")
    readlines()
    print()
    print("********************************************")
    print("Readline")
    print("********************************************")
    readline()
    print()
    print("********************************************")
    print("Iterate over file object")
    print("********************************************")
    iterate_over_file_object()


def readlines():
    # possible memory overload
        try:
            with open(os.path.join("data", "contacts.csv"), encoding="latin_1") as file:
                lines = file.readlines()

                for line in lines:
                    print(line.strip())
        except FileNotFoundError:
            print("Error: File not found")
            exit(1)
        except PermissionError:
            print("Error: Permission denied")
            exit(1)


def readline():
    # read line by line
    try:
        with open(os.path.join("data", "contacts.csv"), encoding="latin_1") as file:
            print(file.readline().strip())
            print(file.readline().strip())
            print(file.readline().strip())
    except FileNotFoundError:
            print("Error: File not found")
            exit(1)
    except PermissionError:
        print("Error: Permission denied")
        exit(1)


def iterate_over_file_object():
    # more efficient memory usage
    try:
        with open(os.path.join("data", "contacts.csv"), encoding="latin_1") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print("Error: File not found")
        exit(1)
    except PermissionError:
        print("Error: Permission denied")
        exit(1)


if __name__ == "__main__":
    main()
