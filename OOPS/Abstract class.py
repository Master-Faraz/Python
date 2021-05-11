# .              Creating costum exception ->    Class name must end with Error
# .              and Exception is passed as an argument

from abc import ABC, abstractmethod


class Invalid_Error(Exception):
    pass


class Stream(ABC):

    def __init__(self) -> None:  # .         Making stream close
        self.condition = False

    def open(self):  # .              Checking if stream is already opened or not
        if self.condition:
            raise Invalid_Error("Stream is already present")
        else:
            self.condition = True

    def close(self):
        if not self.condition:
            raise Invalid_Error("Stream is already Closed")
        else:
            self.condition = False

    @abstractmethod
    def read(self):
        pass


class File_Stream(Stream):
    def read(self):
        print("Reading data from file")


class Network_Stream(Stream):
    def read(self):
        print("Reading data from Network")


obj = Stream()
obj.open()
