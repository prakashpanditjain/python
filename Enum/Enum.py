from enum import IntEnum
from enum import StrEnum


class myclass(StrEnum):
    MySQL = "MySQL"
    PostgreSQL = "PostgreSQL"
    SQLITE = "SQLITE"
    MONGODB = "MONGODB"


class cls_enum_type(IntEnum):
    myage = 30
    myheight = 163
    mysalary = 10000000


if __name__ == '__main__':
    print(myclass.MONGODB)
    for db in myclass:
        print(db)