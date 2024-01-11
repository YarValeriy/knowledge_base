from classes.field import Field
import classes.exceptions as ex

class Phone(Field):
    def __init__(self, value):
        self._value = None
        self.value = value
        super().__init__(self._value)

    @property
    def value(self):
        return self._value
    
    @Field.value.setter
    def value(self, phone):
        if phone.isdigit() and len(phone) == 10:
            self._value = phone
        else:
            raise ex.NotCorrectPhone

    def validate(self, phone):
        if phone.isdigit() and len(phone) == 10:
            return True
        return False