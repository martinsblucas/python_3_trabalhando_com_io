import os


def main():
    write_in_file()
    write_new_file()


def write_in_file():
    try:
        with open(os.path.join("data", "contacts-write.csv"), encoding="latin_1", mode="a") as file:
            file.write("12,Vera,vera@vera\n")
    except PermissionError:
        print("Error: Permission denied")
        exit(1)


def write_new_file():
    try:
        with open(os.path.join("data", "contacts-new.csv"), mode="w+") as file:
            contacts = ["1,Lucas,lucas@lucas.com",
                        "2,Anderson,anderson@anderson.com",
                        "3,Antonio,antonio@antonio.com"]
            for contact in contacts:
                file.write(f"{contact}\n")
            
            file.flush()
            file.seek(0)

            for line in file:
                print(line, end="")
    except PermissionError:
        print("Error: Permission denied")
        exit(1)


if __name__ == "__main__":
    main()
