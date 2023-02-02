import cv2
import mediapipe as mp
import time

class HandsDetection():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands = mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode, self.maxHands,
                                      self.detectionCon, self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self, image, draw=True):
        imgRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return image

def main():
    pTime = 0
    cTime= 0

    cap = cv2.VideoCapture(0)
    detector = HandsDetection()

    while True:
        success, image = cap.read()
        image = detector.findHands(image)
        cTime = time.time()
        fps = 1 / (cTime-pTime)
        pTime = cTime

        cv2.putText(image, str(int(fps)), (10,70),
                    cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 3)

        cv2.imshow('Hands Detection', image)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break



