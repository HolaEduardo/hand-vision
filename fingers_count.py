import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Índices de los landmarks para las puntas de los dedos
fingers_tips_ids = [4, 8, 12, 16, 20]

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Para el pulgar
            if landmarks[fingers_tips_ids[0]].x < landmarks[fingers_tips_ids[0] - 1].x:
                finger_count += 1

            # Para los otros 4 dedos
            for tip_id in fingers_tips_ids[1:]:
                if landmarks[tip_id].y < landmarks[tip_id - 2].y:
                    finger_count += 1

            # Mostrar conteo en pantalla
            cv2.putText(frame, f"Dedos levantados: {finger_count}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Conteo de Dedos", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
