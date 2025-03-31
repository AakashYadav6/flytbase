from unittest import TestCase
from unittest.mock import patch
from src.query_interface import check_mission_status

class TestQueryInterface(TestCase):
    @patch('builtins.input', side_effect=["01:00", "01:10", "10 15 5 01:01", "15 20 8 01:05", "32 43 6 01:07", "43 52 20 01:09", "done"])
    def test_mission_status(self, mock_input):
        conflicts = check_mission_status()
        self.assertIsInstance(conflicts, list)

if __name__ == '__main__':
    unittest.main()

