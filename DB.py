import os
from abc import ABC, abstractmethod
from typing import List


class Database(ABC):
    """
    Database is an abstract class that defines the interface for a key-value database.
    """

    @abstractmethod
    def get(self, key) -> str:
        """
        get returns the value for the given key.
        """
        pass

    @abstractmethod
    def set(self, key, value):
        """
        set sets the value for the given key.
        """
        pass

    @abstractmethod
    def delete(self, key):
        """
        delete deletes the given key.
        """
        pass

    @abstractmethod
    def list_keys(self) -> List[str]:
        """
        list_keys returns a list of all keys in the database.
        """
        pass


FILE_DB_DELIMITER = "::"


class FileDB(Database):
    """
    FileDB is a simple key-value database that stores data in a file on disk.
    """

    def __init__(self, filename):
        self.filename = filename
        self.delimiter = FILE_DB_DELIMITER
        self.data = self._read_file()

    def _read_file(self):
        """
        _read_file reads the file and returns a dictionary of key-value pairs.
        """

        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    key, value = line.strip().split(self.delimiter, 1)
                    data[int(key)] = value
        return data

    def _write_file(self):
        """
        _write_file writes the dictionary of key-value pairs to the file.
        """

        with open(self.filename, "w") as f:
            for key, value in self.data.items():
                f.write(f"{key}{self.delimiter}{value}\n")

    def get(self, key: str):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self._write_file()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self._write_file()

    def list_keys(self):
        return list(self.data.keys())
