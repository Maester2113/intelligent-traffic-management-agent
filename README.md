Intelligent Traffic Management Agent

An AI-powered smart traffic control system that dynamically manages traffic signals using real-time video feeds and intelligent agent-based decision making.

📌 Overview

This project simulates a smart traffic intersection with 4 lanes. It uses computer vision and AI techniques to:

Detect vehicles in each lane
Assign priority based on traffic density
Dynamically control traffic lights
Prevent starvation using queue-based scheduling
Detect emergency vehicles (e.g., ambulances) and prioritize them
🧠 Key Features
🚗 Vehicle Detection using YOLOv8
📊 Dynamic Signal Timing based on vehicle count
⚖️ Weighted Scoring Algorithm for fair lane selection
🔁 Queue Mechanism to avoid starvation
🚑 Ambulance Detection & Priority Override
🎥 Real-time Video Processing with OpenCV
🌐 Web Interface using Flask for live monitoring


System Architecture
Video Input (4 Lanes)
        ↓
Computer Vision (YOLOv8)
        ↓
Vehicle Counting & Classification
        ↓
Score Calculation (Weights + Density)
        ↓
Agent Decision Logic
        ↓
Traffic Light Control
        ↓
Flask Web Dashboard (Live Feed)


⚙️ Tech Stack
Python
OpenCV
YOLOv8 (Ultralytics)
Flask
NumPy


📂 Project Structure
intelligent-traffic-management-agent/
│
├── backend/
│   ├── app.py              # Flask server
│   ├── logic.py            # Core traffic agent logic
│   └── model/              # YOLO model files
│
├── frontend/
│   └── index.html          # Web UI
│
├── videos/                 # Input traffic videos
├── requirements.txt
└── README.md
