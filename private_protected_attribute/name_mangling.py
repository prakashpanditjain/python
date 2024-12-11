class myclass():
    def __init__(self):
        self.__variable = 20

object = myclass()

print(object._myclass__variable)

class private_class():
    def __init__(self,__name, __address):
        self.__name = __name
        self.__address = __address

    # @classmethod
    def call_private(self) -> None:
        _name = self.__name
        _address = self.__address
        print(_name,'\n',_address)
        # return _name


obj = private_class("prakash","At post Naichakur Tq omerga Dist Osmanabad 413606")
print(obj.call_private())
print(obj._private_class__address)