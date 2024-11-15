import cv2
import face_recognition
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
MOTOR_PIN = 18      # Pin for motor control
BUZZER_PIN = 23     # Pin for buzzer alarm
GPIO.setup(MOTOR_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Load known face encodings (for simplicity, only one known face here)
known_face_encodings = []
known_face_names = ["Owner"]

def register_owner():
    camera = cv2.VideoCapture(0)
    print("Registering owner, please look at the camera...")
    ret, frame = camera.read()
    if ret:
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        if face_encodings:
            known_face_encodings.append(face_encodings[0])
            print("Owner registered successfully!")
        else:
            print("No face detected. Try again.")
    camera.release()

def recognize_face():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            print("Access Granted!")
            start_vehicle()
        else:
            print("Unauthorized access!")
            unauthorized_alert()
    camera.release()

def start_vehicle():
    print("Vehicle started.")
    GPIO.output(MOTOR_PIN, GPIO.HIGH)
    time.sleep(5)  # Simulate vehicle running for 5 seconds
    stop_vehicle()

def stop_vehicle():
    print("Vehicle stopped.")
    GPIO.output(MOTOR_PIN, GPIO.LOW)

def unauthorized_alert():
    print("Unauthorized access detected! Buzzer activated.")
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

try:
    register_owner()
    input("Press Enter to start recognition...")
    recognize_face()
finally:
    GPIO.cleanup()
    print("GPIO cleanup complete.")
