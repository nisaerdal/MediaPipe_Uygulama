import cv2
import mediapipe as mp
import config
class HandsDetection():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        int(self.detectionCon), int(self.trackCon))

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, image, draw=True):
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(image, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return image


def main():
    detector = HandsDetection()
    #cap = cv2.VideoCapture(config.video_file)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output_frame = detector.findHands(frame)
        cv2.imshow('Hand Detection', output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
main()