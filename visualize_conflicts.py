import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def plot_conflicts(missions, conflicts):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    cmap = cm.get_cmap('viridis')  # Color map for time representation
    norm = mcolors.Normalize(vmin=0, vmax=24*60)  # Normalize time to minutes
    
    for mission in missions:
        waypoints = mission['waypoints']
        times = [convert_time_to_minutes(wp['time']) for wp in waypoints]
        colors = [cmap(norm(t)) for t in times]
        
        xs, ys, zs = zip(*[(wp['x'], wp['y'], wp['z']) for wp in waypoints])
        
        ax.scatter(xs, ys, zs, c=colors, label=mission['name'], marker='o', s=50)
        ax.plot(xs, ys, zs, color='gray', linestyle='dashed')
    
    # Plot conflicts in red
    for conflict in conflicts:
        ax.scatter(conflict['x'], conflict['y'], conflict['z'], c='red', marker='X', s=100, label='Conflict')
    
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')
    plt.title('UAV Conflict Visualization in 4D')
    plt.legend()
    plt.show()

def convert_time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

if __name__ == "__main__":
    missions = [
        {"name": "Drone_Alpha", "waypoints": [
            {"x": 10, "y": 15, "z": 5, "time": "01:01"},
            {"x": 15, "y": 20, "z": 8, "time": "01:05"}
        ]},
        {"name": "Drone_Gamma", "waypoints": [
            {"x": 10, "y": 15, "z": 5, "time": "01:01"},
            {"x": 15, "y": 20, "z": 8, "time": "01:05"}
        ]},
        {"name": "Drone_Theta", "waypoints": [
            {"x": 10, "y": 20, "z": 5, "time": "01:05"}
        ]}
    ]
    
    conflicts = [
        {"x": 10, "y": 15, "z": 5, "time": "01:01"},
        {"x": 15, "y": 20, "z": 8, "time": "01:05"},
        {"x": 10, "y": 20, "z": 5, "time": "01:05"}
    ]
    
    plot_conflicts(missions, conflicts)

