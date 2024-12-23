import mediapipe as mp
import cv2 as cv

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

vid = cv.VideoCapture(0, cv.CAP_DSHOW)
s=0.5
while True:
    bool, frame = vid.read()
    frame = cv.resize(frame, (int(frame.shape[1] * s), int(frame.shape[0] * s)), interpolation=cv.INTER_AREA)
    frame = cv.flip(frame, 1)
    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = hands.process(rgb)
    coords = result.multi_hand_landmarks
    print(coords)
    if coords:
        for hand in coords:
            mpdraw.draw_landmarks(frame, hand, mphands.HAND_CONNECTIONS)
            cv.imshow('yes', frame)
            cv.waitKey(10)
vid.release()
cv.destroyAllWindows()
