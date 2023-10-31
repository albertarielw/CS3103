import os
from abc import ABC, abstractmethod
from typing import List


class Database(ABC):
    @abstractmethod
    def get(self, key) -> str:
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def list_keys(self) -> List[str]:
        pass


FILE_DB_DELIMITER = "::"


class FileDB(Database):
    def __init__(self, filename):
        self.filename = filename
        self.delimiter = FILE_DB_DELIMITER
        self.data = self._read_file()

    def _read_file(self):
        data = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    key, value = line.strip().split(self.delimiter, 1)
                    data[int(key)] = value
        return data

    def _write_file(self):
        with open(self.filename, "w") as f:
            for key, value in self.data.items():
                f.write(f"{key}{self.delimiter}{value}\n")

    def get(self, key):
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
