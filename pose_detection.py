import cv2
import mediapipe as mp

class PoseDetection:
    def __init__(self, mode=False, upBody = False,smooth= True,
                 detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.pose_drawing = mp.solutions.drawing_utils
        self.pose_drawing_styles = mp.solutions.drawing_styles
        self.pose = mp.solutions.pose.Pose(self.mode, self.upBody, self.smooth,
                                           int(self.detectionCon), int(self.trackCon))

    def findPose(self, image, draw=True):
        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(imgRGB)
        if results.pose_landmarks:
            if draw:
                self.pose_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    self.pose.POSE_CONNECTIONS
                )
        return image

def main():
    detector = PoseDetection()
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output_frame = detector.findPose(frame)
        cv2.imshow('Pose Detection', output_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()