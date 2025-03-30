import unittest
from src.conflict_detection import detect_conflicts

class TestConflictDetection(unittest.TestCase):
    def test_conflict_detection(self):
        primary_mission = {
            "start_time": "01:00",
            "end_time": "01:30",
            "waypoints": [
                {"x": 20, "y": 25, "z": 10, "time": "01:10"}
            ]
        }
        flight_data = {"drones": [{
            "Drone_Name": "Drone_Gamma",
            "Waypoints": [{"X": 20, "Y": 25, "Z": 10, "Time": "01:10"}]
        }]}
        
        conflicts = detect_conflicts(primary_mission, flight_data)
        self.assertGreater(len(conflicts), 0)

if __name__ == '__main__':
    unittest.main()

