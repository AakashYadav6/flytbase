<<<<<<< HEAD
=======
# flytbase
>>>>>>> 2af0a53d (Added UAV conflict detection system)
# UAV Flight Conflict Detection System

## Overview
This project provides a conflict detection system for UAV (Unmanned Aerial Vehicle) flight missions. It allows users to enter a primary mission's waypoints and checks for potential conflicts with existing flight data.

## Setup Instructions

### **1. Clone the Repository**  
Open a terminal and run:  
```bash
git clone <repo-url>
cd uav_flytbase
```

### **2. Create a Virtual Environment**  
Create and activate a Python virtual environment:  
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3. Install Dependencies**  
Ensure you have a `requirements.txt` file in the repository. Then, install the dependencies:  
```bash
pip install -r requirements.txt
```

## Directory Structure  
Ensure the following directory structure is maintained:
```
/uav_flytbase/
│── src/
│   ├── query_interface.py
│   ├── conflict_detection.py
│   ├── get_primary_mission.py
│── data/
│   ├── uav_flight_data_extended.json
```

## Run the System  
Navigate to the project root directory and run the following command:
```bash
python src/query_interface.py
```

## Execution Example  
After running the above command, follow the prompts:
```bash
Enter mission start time (HH:MM): 01:00
Enter mission end time (HH:MM): 01:20

Enter waypoints in the format: X Y Z Time (Enter 'done' to finish)
Enter waypoint (or 'done' to stop): 10 15 5 01:01
Enter waypoint (or 'done' to stop): 15 20 8 01:05
Enter waypoint (or 'done' to stop): 25 30 12 01:15
Enter waypoint (or 'done' to stop): 45 50 14 01:19
Enter waypoint (or 'done' to stop): done
```
The system will then check for conflicts and visualize the mission.

## Features  
- User-friendly CLI for entering UAV flight waypoints.
- Conflict detection based on pre-existing flight data.
- 3D visualization of flight paths and detected conflicts.
- Time-based simulation of UAV missions.

## Notes  
- The flight data file (`uav_flight_data_extended.json`) should contain existing UAV flight paths in JSON format.
- Ensure that the system has read access to the `data/` directory.

## Troubleshooting  
- **File Not Found Error:** Ensure that `uav_flight_data_extended.json` is in the `data/` directory.
- **Incorrect Time Format:** Ensure time inputs follow `HH:MM` format.

For any additional support, feel free to reach out!

