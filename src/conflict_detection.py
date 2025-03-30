import json

def load_flight_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def convert_time_to_minutes(time_str):
    """Convert time in HH:MM format to minutes since midnight."""
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def detect_conflicts(primary_mission, flight_data, buffer=5, time_window=2):
    """
    Detects conflicts between primary mission waypoints and drone flight data
    using a buffer for spatial proximity and a time window for temporal proximity.

    :param primary_mission: The primary mission data containing waypoints.
    :param flight_data: The flight data of drones containing their waypoints.
    :param buffer: The maximum allowed spatial proximity between drones and waypoints (in meters).
    :param time_window: The maximum allowed time difference between waypoints (in minutes).
    :return: A list of conflicts detected.
    """
    conflicts = []
    
    for drone in flight_data["drones"]:
        for wp in drone["Waypoints"]:
            for primary_wp in primary_mission["waypoints"]:
                
                # Check if the spatial distance is within the buffer zone
                spatial_condition = (
                    abs(primary_wp['x'] - wp['X']) <= buffer and
                    abs(primary_wp['y'] - wp['Y']) <= buffer and
                    abs(primary_wp['z'] - wp['Z']) <= buffer
                )
                
                # Convert time strings to minutes
                primary_wp_time_in_minutes = convert_time_to_minutes(primary_wp['time'])
                wp_time_in_minutes = convert_time_to_minutes(wp['Time'])
                
                # Check if the time difference is within the time window
                time_condition = (
                    abs(primary_wp_time_in_minutes - wp_time_in_minutes) <= time_window
                )
                
                # If both spatial and temporal conditions are satisfied, there's a conflict
                if spatial_condition and time_condition:
                    conflicts.append({
                        "conflicting_drone": drone["Drone_Name"],
                        "location": (wp['X'], wp['Y'], wp['Z']),
                        "time": wp['Time']
                    })
                    
    return conflicts

