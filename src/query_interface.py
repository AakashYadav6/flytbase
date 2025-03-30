import json
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import CubicSpline
from get_primary_mission import get_primary_mission
from conflict_detection import detect_conflicts, load_flight_data
from datetime import datetime

def check_mission_status():
    """Checks for mission conflicts and visualizes the UAV mission."""
    flight_data = load_flight_data("data/uav_flight_data_extended.json")
    primary_mission = get_primary_mission()
    
    conflicts = detect_conflicts(primary_mission, flight_data)
    
    if conflicts:
        print("Conflict Detected!")
        for conflict in conflicts:
            print(f"Conflict with {conflict['conflicting_drone']} at {conflict['location']} at {conflict['time']}")
    else:
        print("Mission is clear.")
    
    visualize_mission(primary_mission, conflicts)
    return conflicts

def time_to_minutes(time_str):
    """Converts HH:MM format to total minutes."""
    hh, mm = map(int, time_str.split(":"))
    return hh * 60 + mm

def interpolate_trajectory(primary_waypoints):
    """Interpolates UAV trajectory using cubic splines for a smooth path."""
    x = primary_waypoints[:, 0]
    y = primary_waypoints[:, 1]
    z = primary_waypoints[:, 2]
    
    spline_x = CubicSpline(np.arange(len(x)), x)
    spline_y = CubicSpline(np.arange(len(y)), y)
    spline_z = CubicSpline(np.arange(len(z)), z)
    
    new_time = np.linspace(0, len(x) - 1, 500)
    smooth_x = spline_x(new_time)
    smooth_y = spline_y(new_time)
    smooth_z = spline_z(new_time)
    
    return smooth_x, smooth_y, smooth_z

def visualize_mission(primary_mission, conflicts):
    """Visualizes the UAV mission with potential conflict points."""
    primary_waypoints = np.array([[wp['x'], wp['y'], wp['z']] for wp in primary_mission['waypoints']])
    primary_times = np.array([time_to_minutes(wp['time']) for wp in primary_mission['waypoints']])
    
    mission_start_time = time_to_minutes(primary_mission['start_time'])
    mission_end_time = time_to_minutes(primary_mission['end_time'])
    
    scaling_factor = 10  # Adjust this for simulation speed
    total_mission_duration = mission_end_time - mission_start_time
    scaled_duration = total_mission_duration / scaling_factor
    
    smooth_x, smooth_y, smooth_z = interpolate_trajectory(primary_waypoints)
    
    conflict_points = np.array([[conflict['location'][0], conflict['location'][1], conflict['location'][2]] for conflict in conflicts]) if conflicts else np.array([])
    conflict_times = np.array([time_to_minutes(conflict['time']) for conflict in conflicts]) if conflicts else np.array([])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter3d(
        x=smooth_x, y=smooth_y, z=smooth_z,
        mode='lines',
        line=dict(color='green', width=4),
        name="Primary UAV Path"
    ))
    
    fig.add_trace(go.Scatter3d(
        x=primary_waypoints[:, 0],
        y=primary_waypoints[:, 1],
        z=primary_waypoints[:, 2],
        mode='markers',
        marker=dict(color='blue', size=8, symbol='cross'),
        name="Waypoints"
    ))
    
    if conflicts:
        fig.add_trace(go.Scatter3d(
            x=conflict_points[:, 0],
            y=conflict_points[:, 1],
            z=conflict_points[:, 2],
            mode='markers',
            marker=dict(color='red', size=10),
            name="Conflict Points"
        ))
    
    fig.update_layout(
        title="Primary UAV Mission and Conflict Visualization",
        scene=dict(
            xaxis_title="X Coordinate",
            yaxis_title="Y Coordinate",
            zaxis_title="Z Coordinate"
        ),
        showlegend=True
    )
    
    fig.show()

if __name__ == "__main__":
    check_mission_status()

