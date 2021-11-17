import os
import csv
import pickle
import json
import contact


def main():
    contacts = instantiate_contacts_from_csv(os.path.join("data",  "contacts.csv"))
    contacts = [contact for contact in contacts]
    create_pickle_from_contacts(contacts, os.path.join("data",  "contacts.p"))
    create_json_from_contacts(contacts, os.path.join("data",  "contacts.json"))

    print()
    print("**************************************** ")
    print("CSV")
    print("**************************************** ")
    print()
    for line in contacts:
        print()
        print("**************************************** ")
        print("ID ..................................... ", line.id)
        print("Name: .................................. ", line.name)
        print("Email: ................................. ", line.email)
        print("**************************************** ")
        print()

    print()
    print("**************************************** ")
    print("PICKLE")
    print("**************************************** ")
    print()
    contacts = get_contacts_from_pickle(os.path.join("data",  "contacts.p"))
    for line in contacts:
        print()
        print("**************************************** ")
        print("ID ..................................... ", line.id)
        print("Name: .................................. ", line.name)
        print("Email: ................................. ", line.email)
        print("**************************************** ")
        print()

    print()
    print("**************************************** ")
    print("JSON")
    print("**************************************** ")
    print()
    contacts = get_contacts_from_json(os.path.join("data",  "contacts.json"))
    for line in contacts:
        print()
        print("**************************************** ")
        print("ID ..................................... ", line.id)
        print("Name: .................................. ", line.name)
        print("Email: ................................. ", line.email)
        print("**************************************** ")
        print()


def instantiate_contacts_from_csv(path):
    csv_content = get_contacts_from_csv(path)
    for item in csv_content:
        id, name, email = item
        yield contact.Contact(id=id, name=name, email=email)


def create_pickle_from_contacts(contacts, path):
    try:
        with open(path, mode="wb") as file:
            pickle.dump([contact for contact in contacts], file)
    except PermissionError:
        print("Error: persmission denied")


def create_json_from_contacts(contacts, path):
    try:
        with open(path, mode="w", encoding="latin_1") as file:
            default = lambda contact: {"id": contact.id,
                                       "name": contact.name, 
                                       "email": contact.email}
            json.dump(contacts, file, default=default)
    except PermissionError:
        print("Error: persmission denied")


def get_contacts_from_csv(path):
    try:
        with open(path, encoding="latin_1") as file:
            csv_reader = csv.reader(file)
            for line in csv_reader:
                yield line
    except FileNotFoundError:
        print("Error: file not found")


def get_contacts_from_pickle(path):
    try:
        with open(path, mode="rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("Error: file not found")


def get_contacts_from_json(path):
    try:
        with open(path, mode="r") as file:
            return [contact.Contact(**item) for item in json.load(file)]
    except FileNotFoundError:
        print("Error: file not found")


if __name__ == "__main__":
    main()
