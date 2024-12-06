from enum import IntEnum
from enum import StrEnum
from enum import auto


class Role(StrEnum):
    ADMIN: str = 'admin'
    USER: str = 'user'
    USER2: str = 'user2'
    MANAGER: str = 'manager'


role: Role = Role.ADMIN
print(role)


class associated_value(IntEnum):
    OKSTATUS = 200
    NOT_FOUND = 404
    GET_WAY_ERROR = 502


webpage: associated_value = associated_value.NOT_FOUND
print(webpage)


class autoclass(IntEnum):
    OKSTATUS = auto()
    NOT_FOUND = auto()
    GET_WAY_ERROR = auto()


object_ofAuto: autoclass = autoclass.NOT_FOUND
print(object_ofAuto)


class autoclass(StrEnum):
    OKSTATUS = auto()
    NOT_FOUND = auto()
    GET_WAY_ERROR = auto()


object_ofAuto: autoclass = autoclass.NOT_FOUND
print(object_ofAuto)
