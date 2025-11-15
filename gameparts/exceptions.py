class FieldIndexError(IndexError):
    def __str__(self):
        return "Введено значение за пределами игрового поля"


class FieldNotEmptyError(Exception):
    def __str__(self):
        return "Клетка занята"
