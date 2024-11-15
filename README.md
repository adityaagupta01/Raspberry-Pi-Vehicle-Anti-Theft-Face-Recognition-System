
# Raspberry Pi Vehicle Anti-Theft Face Recognition System

This project implements a security system for vehicles using a Raspberry Pi. It uses face recognition technology to grant access to authorized users only. Unauthorized access attempts trigger an alarm, making it a robust anti-theft solution for modern vehicles.

## Features
- **Face Recognition**: Recognizes registered users' faces to allow vehicle access.
- **LCD Display**: Shows system status messages, such as "Access Granted" or "Unauthorized Access."
- **Buzzer Alarm**: Triggers a buzzer for unauthorized access attempts.
- **Motor Control**: Controls the vehicle start/stop actions based on user authentication.

## Project Components
- **Raspberry Pi 3** (or compatible model)
- **24x4 LCD Display**: For displaying system messages.
- **Camera Module**: Captures faces for recognition.
- **DC Motor**: Simulates vehicle start/stop.
- **Buzzer**: Sounds an alarm when unauthorized access is detected.
- **Additional Components**: Resistors, connecting wires, GPIO setup.

## Software Requirements
- **Operating System**: Raspbian OS or any compatible Linux distribution.
- **Programming Language**: Python 3
- **Libraries**:
  - `face_recognition` for facial detection and recognition
  - `OpenCV` for image processing
  - `RPi.GPIO` for GPIO control

## Setup Instructions

1. **Install Necessary Libraries**:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-opencv
   sudo pip3 install face_recognition
   ```

2. **Connect Hardware Components**:
   - Connect the camera module to the Raspberry Pi’s camera port.
   - Connect the LCD display, buzzer, and motor to the appropriate GPIO pins.

3. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Vehicle-Anti-Theft-System.git
   cd Vehicle-Anti-Theft-System
   ```

4. **Run the Code**:
   ```bash
   python3 anti_theft_system.py
   ```

## Code Overview
- **anti_theft_system.py**: Main script that handles face registration, recognition, motor control, and alarm activation.

## Circuit Diagram
Refer to the image provided in the repository for the circuit layout and wiring instructions.

## Usage
1. Register the authorized user’s face.
2. Use the system to recognize users and control vehicle access.
3. In case of unauthorized access, the buzzer will sound an alert.

## Future Improvements
- Adding SMS/email alerts for unauthorized access.
- Integrating GPS to locate the vehicle if stolen.
- Adding a database for multiple users.

