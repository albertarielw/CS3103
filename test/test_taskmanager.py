import unittest
from unittest.mock import MagicMock, patch
from Taskmanager import TaskManager, TaskResult
from multiprocessing import Queue
from DB import Database, FileDB
import time


class MockDB(Database):
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def delete(self, key):
        pass

    def list_keys(self):
        pass


def mock_function(url):
    # A simple mock function that returns a TaskResult
    time.sleep(1)
    result = TaskResult(
        url=url,
        ip_addr="127.0.0.1",
        geolocation="local",
        next_urls=[],
        rtt=1.0,
    )
    return result


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.db = MockDB()
        self.seed = [
            "http://www.example.com",
        ]

    def test_task_manager(self):
        task_manager = TaskManager(
            self.db, mock_function, self.seed, timeout=5, num_procs=2
        )
        task_manager.start()

        # Assertions
        self.assertEqual(
            self.db.get(0), "http://www.example.com;;127.0.0.1;;local;;1.0"
        )
        self.assertFalse(task_manager.timed_out())


if __name__ == "__main__":
    unittest.main()
