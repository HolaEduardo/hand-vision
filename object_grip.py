import cv2
import mediapipe as mp
import math

def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            thumb_index_dist = distance(lm[4], lm[8])        # pulgar a índice
            index_tip_palm = distance(lm[8], lm[0])          # índice a muñeca
            middle_tip_palm = distance(lm[12], lm[0])        # medio a muñeca
            ring_tip_palm = distance(lm[16], lm[0])          # anular a muñeca
            pinky_tip_palm = distance(lm[20], lm[0])         # meñique a muñeca

            # Mostrar valores
            cv2.putText(frame, f"Thumb-Index: {thumb_index_dist:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

            # Heurística para detectar agarre
            if (0.08 < thumb_index_dist < 0.25 and
                    0.18 < index_tip_palm < 0.42 and
                    0.18 < middle_tip_palm < 0.42 and
                    0.18 < ring_tip_palm < 0.42 and
                    0.18 < pinky_tip_palm < 0.42):

                cv2.putText(frame, 'Agarrando objeto', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'No en agarre', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Detección de Agarre", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
