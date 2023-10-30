import unittest
import os
from DB import FileDB


class TestFileDB(unittest.TestCase):
    def setUp(self):
        self.db = FileDB("test_database.txt")
        self.test_data = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }
        for key, value in self.test_data.items():
            self.db.set(key, value)

    def tearDown(self):
        if os.path.exists("test_database.txt"):
            os.remove("test_database.txt")

    def test_get(self):
        for key, value in self.test_data.items():
            self.assertEqual(self.db.get(key), value)
        self.assertIsNone(self.db.get("nonexistent_key"))

    def test_set(self):
        self.db.set("new_key", "new_value")
        self.assertEqual(self.db.get("new_key"), "new_value")

    def test_delete(self):
        self.db.delete("key1")
        self.assertIsNone(self.db.get("key1"))
        self.db.delete("nonexistent_key")  # Should not raise an error

    def test_list_keys(self):
        self.assertEqual(sorted(self.db.list_keys()), sorted(self.test_data.keys()))


if __name__ == "__main__":
    unittest.main()
