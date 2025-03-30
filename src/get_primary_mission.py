def get_primary_mission():
    """
    Takes user input to define the primary drone's mission waypoints in a single-line format.

    Returns:
        dict: Dictionary containing waypoints and mission time window.
    """
    waypoints = []

    start_time = input("Enter mission start time (HH:MM): ")
    end_time = input("Enter mission end time (HH:MM): ")

    print("\nEnter waypoints in the format: X Y Z Time (Enter 'done' to finish)")
    while True:
        waypoint_input = input("Enter waypoint (or 'done' to stop): ").strip()
        if waypoint_input.lower() == 'done':
            break

        try:
            x, y, z, time = waypoint_input.split()
            waypoints.append({
                'x': float(x),
                'y': float(y),
                'z': float(z),
                'time': time
            })
        except ValueError:
            print("Invalid format! Please enter in 'X Y Z Time' format.")

    return {
        'start_time': start_time,
        'end_time': end_time,
        'waypoints': waypoints
    }


if __name__ == "__main__":
    primary_mission = get_primary_mission()
    print("\nPrimary Mission Data:")
    print(primary_mission)

