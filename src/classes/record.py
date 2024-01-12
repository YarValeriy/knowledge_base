from datetime import date, datetime
from classes.name import Name
from classes.phone import Phone
from classes.birthday import Birthday


class Record():
    def __init__(self, name, date=None):
        self.name = Name(name)  # Mandatory
        self.phones = []
        self.date = Birthday(date)


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def days_to_birthday(self):
        if self.date.value != None:
            today = date.today()
            bdat = datetime.strptime(self.date.value, '%d-%m-%Y')
            birthday = datetime(year=today.year, month=bdat.month, day=bdat.day)
            curdat = datetime(year=today.year, month=today.month, day=today.day)
            count = (curdat - birthday).days
            count = count if count > 0 else abs(count)
            return f"{count} days left to birthday."
        else:
            return f"Birthday data is misssing."


    def edit_phone(self, phone, phone_new):
        # phone_obj = self.find_phone(phone)
        phone_obj: Phone = self.find_phone(phone)
        if phone_obj and phone_obj.validate(phone_new):
            phone_obj.value = phone_new
        else:
            raise ValueError


    def remove_phone(self, phone_r):
        p_obj = self.find_phone(phone_r)
        if p_obj:
            self.phones.remove(p_obj)


    def find_phone(self, phone_f):
        for phone in self.phones:
            if phone.value == phone_f: return phone


    def __str__(self):
        str_dat = f"; birthday: {self.date.value}" if self.date.value != None else ""
        return f"Name: {self.name.value.title()}; phones: {'; '.join(p.value for p in self.phones)} {str_dat}"