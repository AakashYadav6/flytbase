import unittest
from src.query_interface import check_mission_status

class TestQueryInterface(unittest.TestCase):
    def test_mission_status(self):
        conflicts = check_mission_status()
        self.assertIsInstance(conflicts, list)

if __name__ == '__main__':
    unittest.main()

