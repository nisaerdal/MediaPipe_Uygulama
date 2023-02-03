import cv2
import config
import mediapipe as mp
import numpy as np
class HolisticDetection():
    def __init__(self,static_image_mode=True,model_complexity=2,refine_face_landmarks=True,
                min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.refine_face_landmarks = refine_face_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mpHolistic = mp.solutions.holistic
        self.holistic = self.mpHolistic.Holistic()

    def findHolistic(self, image, draw=True):
        if not image.size:
            return None
        """
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.holistic.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        """
        image_height, image_width, _ = image.shape
        results = self.holistic.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if draw:
            self.mp_drawing.draw_landmarks(
                results.face_landmarks,
                results.pose_landmarks,
                self.mpHolistic.FACEMESH_CONTOURS,
                self.mpHolistic.POSE_CONNECTIONS,
                self.mpHolistic.FACEMESH_TESSELATION,
                #landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style(),
                #connection_drawing_spec = self.mp_drawing_styles.get_default_face_mesh_tesselation_style(),
                #connection_drawing_spec=self.mp_drawing_styles.get_default_face_mesh_contours_style()
            )


def main():
    detector = HolisticDetection()
    cap = cv2.VideoCapture(config.video_file)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        output_frame = detector.findHolistic(frame)
        if output_frame is not None:
            cv2.imshow('Holistic Detection', output_frame)
        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()