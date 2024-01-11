from collections import UserDict
from time import strptime
# from datetime import date, datetime
import pickle
from pathlib import Path
# import classes.exceptions as ex
# from classes.field import Field
# from classes.name import Name
# from classes.phone import Phone
# from classes.birthday import Birthday
from classes.record import Record

class AddressBook(UserDict):
    def __init__(self):
        # self.list_items = []
        self.list_count = 0
        self.data = {}
        self.__abook_file = "book_file.bin"

    def add_record(self, value):
        # self.data[value.name.value] = value.phones
        self.data[value.name.value] = value

    def find(self, name):
        if name in self.data.keys():
            record = Record(name)
            record.phones = self.data[name]
            return self.data.get(name)
        else:
            return None

    def delete(self, name):
        if name in self.data.keys():
            self.data.pop(name)

    def list_creator(self):
        self.list_items = []
        for item in self.data.values():
            self.list_items.append(item)

        self.list_count = len(self.list_items)

    def iterator(self, from_el=0, to_el=2):
        if self.list_count > 0 and from_el < self.list_count:
            return (x for x in self.list_items[from_el:to_el])

    def serialization(self):
        with open(self.__abook_file, "wb") as fh:
            pickle.dump(self.data, fh)

    def check_file_exist(self):
        return Path(self.__abook_file).exists()

    def unserialization(self):
        if self.check_file_exist():
            with open(self.__abook_file, "rb") as fh:
                self.data = pickle.load(fh)
            return self.data

    def search(self, str):
        searched_items = {}
        for val, key in self.data.items():
            if val.find(str) != -1:
                searched_items.update({val: key})
                continue
            for phone in key.phones:
                if phone.value.find(str) != -1:
                    searched_items.update({val: key})
        return searched_items if len(searched_items) > 0 else 0

    def help(self):
        return 

def main():
    pass

if __name__ == "__main__":
    main()