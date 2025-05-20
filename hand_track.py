import cv2
import mediapipe as mp
import numpy as np
from pynput.keyboard import Controller

# 1) Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

# 2) Inicializar cámara y teclado
cap = cv2.VideoCapture(0)
keyboard = Controller()
current_key = None

# 3) Función auxiliar para calcular normal de la palma
def palm_normal(landmarks):
    # Tomamos tres puntos: muñeca, nudillo medio y nudillo meñique
    p0 = np.array([landmarks[mp_hands.HandLandmark.WRIST].x,
                   landmarks[mp_hands.HandLandmark.WRIST].y,
                   landmarks[mp_hands.HandLandmark.WRIST].z])
    p1 = np.array([landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x,
                   landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y,
                   landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].z])
    p2 = np.array([landmarks[mp_hands.HandLandmark.PINKY_MCP].x,
                   landmarks[mp_hands.HandLandmark.PINKY_MCP].y,
                   landmarks[mp_hands.HandLandmark.PINKY_MCP].z])
    v1 = p1 - p0
    v2 = p2 - p0
    n = np.cross(v1, v2)
    return n / np.linalg.norm(n)

# 4) Bucle principal
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip horizontal para que sea tipo “espejo” y convertir a RGB
    frame = cv2.flip(frame, 1)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    direction = None  # tecla a pulsar

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0].landmark
        mp_draw.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

        n = palm_normal(lm)
        nx, ny, nz = n

        tilt_thresh = 0.3
        roll_thresh  = 0.3

        if nz < -tilt_thresh:
            direction = 'w'
        elif nz >  tilt_thresh:
            direction = 's'

        if nx < -roll_thresh:
            direction = 'a'
        elif nx >  roll_thresh:
            direction = 'd'


    # 7) Emular la pulsación
    if direction != current_key:
        if current_key:
            keyboard.release(current_key)
        if direction:
            keyboard.press(direction)
        current_key = direction

    cv2.imshow("Hand Orientation Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
