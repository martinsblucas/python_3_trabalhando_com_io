import os


def main():
    read_from_buffer()
    write_in_buffer()


def read_from_buffer():
    try:
        with open(os.path.join("data", "contacts.csv"), encoding="latin_1") as file:
            print("reading buffered reader .........................", type(file.buffer))
            print()
            print(file.buffer.read().decode("latin_1"))
    except FileNotFoundError:
        print("Error: File not found")
        exit(1)
    except PermissionError:
        print("Error: Permission denied")
        exit(1)


def write_in_buffer():
    try:
        with open(os.path.join("data", "contacts-write.csv"), encoding="latin_1", mode="a+") as file:
            print("reading buffer random ...........................", type(file.buffer))
            file.buffer.write(bytes("13,Verônica,veronica@veronica\n", encoding="latin_1"))
    except PermissionError:
        print("Error: Permission denied")
        exit(1)


if __name__ == "__main__":
    main()
