import cv2
import mediapipe as mp
import time

class PoseDetection():
    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpdraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,
                                     self.detectionCon, self.trackCon)

    def findPose(self, image, draw=True):
        imgRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        if results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(image, results.pose_landmarks,
                                            self.mpPose.POSE_CONNECTIONS)
        return image

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    detector = PoseDetection()
    while True:
        success, image = cap.read()
        image = detector.findPose(image)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(image, str(int(fps)), (70,50),
                    cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)

        cv2.imshow('Pose Detection', image)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            cap.release()
            break